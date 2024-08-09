import os
import gradio as gr
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import base64
import json
import shutil
from tqdm import tqdm
import copy
from configs import config
from utils import *


def save_tag_json(*args):
    # folder_num_path_list+tag_list+note_list+image_path_list+image_tag_list+image_num_list,
    tag_json = load_tag_json()

    args = list(args)
    print("args: ", len(args), args)
    image_num_list = []
    for item in reversed(args):
        if isinstance(item, str):
            image_num_list.insert(0, int(item))
        else:
            break
    print("image_num_list: ", len(image_num_list), image_num_list)
    image_nums = len(image_num_list)
    args = args[:-image_nums]
    slide_id = 3 * image_nums
    print("slide_id: ", slide_id)
    args_front = args[:slide_id]
    args_behind = args[slide_id:]
    print("args_front: ", len(args_front), args_front)
    print("args_behind: ", len(args_behind), args_behind)

    [folder_num_path_list, tag_list, note_list] = chunk_list(args_front, 3)
    [image_path_list, image_tag_list] = chunk_list(args_behind, 2)
    print("folder_num_path_list, tag_list, note_list: ", folder_num_path_list, tag_list, note_list)
    print("image_path_list, image_tag_list: ", image_path_list, image_tag_list)
    image_path_list_temp, image_tag_list_temp = [], []
    for i, (image_path, image_tag) in enumerate(zip(image_path_list, image_tag_list)):
        image_path_list_temp.append(image_path_list[sum(image_num_list[:i]):sum(image_num_list[:i+1])])
        image_tag_list_temp.append(image_tag_list[sum(image_num_list[:i]):sum(image_num_list[:i+1])])
    image_path_list = copy.deepcopy(image_path_list_temp)
    image_tag_list = copy.deepcopy(image_tag_list_temp)

    for img_id, (folder_num_path, tag, note) in enumerate(zip(folder_num_path_list, tag_list, note_list)):
        folder_NPC = folder_num_path.split('/')[-2]
        if folder_NPC not in tag_json:
            tag_json[folder_NPC] = {}
        if folder_num_path not in tag_json[folder_NPC]:
            tag_json[folder_NPC][folder_num_path] = {}
        if "tags_" not in tag_json[folder_NPC][folder_num_path]:
            tag_json[folder_NPC][folder_num_path]["tags_"] = {}
        tag_json[folder_NPC][folder_num_path]["tag"] = 1 if tag else 0
        tag_json[folder_NPC][folder_num_path]["note"] = note
        for (image_path, image_tag) in zip(image_path_list[img_id], image_tag_list[img_id]):
            tag_json[folder_NPC][folder_num_path]["tags_"][image_path] = 1 if image_tag else 0

    with open(config.tag_json_file_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(tag_json, indent=4, ensure_ascii=False))
    
    current_time = get_current_time()
    backup_tag_json_file_path = config.tag_json_file_path.split('.')[0] + current_time + ".json"
    shutil.copy(config.tag_json_file_path, backup_tag_json_file_path)

    good_images_num, all_images_num = save_tag_txt()
    good_images_percentage = round(good_images_num / all_images_num, 4) * 100

    status_code = f"Save tag json to '{config.tag_json_file_path}' done!\nBackup tag json to '{backup_tag_json_file_path}' done!\nSave tag txt to '{config.tag_txt_file_path}' done!\nGood images percentage is {good_images_percentage}% (good images num: {good_images_num} / all images num: {all_images_num})"
    print(f"port: {config.port}\nstatus_code: {status_code}\ntime: {current_time}")

    return status_code, gr.update(choices=sorted(tag_json.keys()))

def pack_tagged_images(pack_root_dir_prefix, NPCs_can_download):
    tag_json = load_tag_json()
    NPCs_can_download.sort()
    pack_root_dir = os.path.normpath(pack_root_dir_prefix) + '_' + '_'.join(NPCs_can_download) + get_current_time()

    for key, value in tag_json.items():
        if key in NPCs_can_download:
            target_NPC_dir = os.path.join(pack_root_dir, key)
            if not os.path.exists(target_NPC_dir):
                os.makedirs(target_NPC_dir, exist_ok=True)
            target_NPC_dir_dirs = os.listdir(target_NPC_dir)
            for k, v in value.items():
                num = k.split('/')[-1]
                if v["tag"] == 0: # unchecked is good image (default)
                    if num not in target_NPC_dir_dirs:
                        shutil.copytree(k, os.path.join(target_NPC_dir, num))
                if v["tag"] == 1: # checked is bad image
                    if num in target_NPC_dir_dirs:
                        shutil.rmtree(os.path.join(target_NPC_dir, num))
    shutil.copy(config.tag_json_file_path, pack_root_dir)
    shutil.make_archive(pack_root_dir, 'zip', pack_root_dir)

    status_code = f"Pack tagged images to '{pack_root_dir}' done!"
    print(f"port: {config.port}\nstatus_code: {status_code}\ntime: {get_current_time()}")

    return status_code

def create_item(folder_NPC, folder_num, card_name, prompts):
    folder_num_path_s, tag_s, note_s, image_path_s, image_tag_s, image_num_s = [], [], [], [], [], []
    tag_json = load_tag_json()
    with gr.Blocks() as submit_item:
        with gr.Row():
            folder_num_path = os.path.join(config.img_root_path, folder_NPC, folder_num)
            folder_num_int = int(folder_num)
            folder_num_card_name = ' '.join([folder_num, card_name])
            with gr.Column(scale=1):
                folder_num_card_name_ = gr.Label(folder_num_card_name, label="folder_num card_name")
                folder_num_path_ = gr.Textbox(folder_num_path, label="folder_num_path", interactive=False, lines=2)
                prompts_ = gr.JSON(prompts, label="prompts", visible=False)
            images = sorted(os.listdir(folder_num_path))
            image_num_ = gr.Label(len(images), label="image_nums", visible=False)

            for image in images:
                with gr.Column(scale=1):
                    image_path = os.path.join(config.img_root_path, folder_NPC, folder_num, image)
                    image_path_ = gr.Textbox(image_path, label="image_path", interactive=False, lines=2, visible=False)
                    # 1. load and show img by .png format
                    # image_ = gr.Image(Image.open(image_path), label=f"{image}", type="pil", interactive=False)
                    # 2.
                    # with open(image_path, 'rb') as f:
                    #     image_data = f.read()
                    # image_bytesio = BytesIO(image_data)
                    # pil_image = Image.open(image_bytesio)
                    # image_ = gr.Image(pil_image, label=f"{image}", type="pil", interactive=False, show_label=False)
                    # 3. load and show img by .webp format
                    img = None
                    try:
                        img = Image.open(image_path)
                    except UnidentifiedImageError as e:
                        print(f"Error opening image {image_path}: {e}")
                    if img is not None:
                        webp_image_bytesio = BytesIO()
                        img.save(webp_image_bytesio, "WEBP")
                        image_ = gr.Image(Image.open(webp_image_bytesio), label=f"{image}", type="pil", interactive=False, show_label=False, show_download_button=False)
                        image_save_value = False
                        if folder_NPC in tag_json and folder_num_path in tag_json[folder_NPC] and image_path in tag_json[folder_NPC][folder_num_path]["tags_"]:
                            image_save_value = True if tag_json[folder_NPC][folder_num_path]["tags_"][image_path] == 1 else False
                        image_tag_ = gr.Checkbox(value=image_save_value, label="bad", interactive=True, visible=config.tag_mode)
                        image_path_s.append(image_path_)
                        image_tag_s.append(image_tag_)

            save_value = False
            note_value = ""
            if folder_NPC in tag_json and folder_num_path in tag_json[folder_NPC]:
                save_value = True if tag_json[folder_NPC][folder_num_path]["tag"] == 1 else False
                note_value = tag_json[folder_NPC][folder_num_path]["note"]
            with gr.Column(scale=1):
                tag_ = gr.Checkbox(value=save_value, label="bad", interactive=True, visible=config.tag_mode)
                note_ = gr.Textbox(value=note_value, label="note", interactive=True, lines=5, visible=config.tag_mode)
            folder_num_path_s.append(folder_num_path_)
            tag_s.append(tag_)
            note_s.append(note_)
            image_num_s.append(image_num_)

    return folder_num_path_s, tag_s, note_s, image_path_s, image_tag_s, image_num_s

def show_image():
    with gr.Blocks() as show_image_blocks:
        folder_num_path_list, tag_list, note_list, image_path_list, image_tag_list, image_num_list = [], [], [], [], [], []
        folder_NPCs = sorted(os.listdir(config.img_root_path)) if config.appointed_NPC_names == [] else config.appointed_NPC_names
        with gr.Row():
            status_ = gr.Textbox(value='', label="status", interactive=False, lines=4)
            status_.value = "Now in tag mode, you can click 'bad' and write in 'note', then click the buttons to save tag json and package good images picked out." if config.tag_mode else "Now in display mode, you can only view the image results, can not tag."
        with gr.Row():
            with gr.Column():
                save_tag_json_ = gr.Button("Save tag json", visible=config.tag_mode)
                tag_json_ = gr.JSON(label="tag json", show_label=False, visible=False)
            with gr.Column():
                pack_root_dir_prefix_ = gr.Textbox(value=config.img_root_path, label="pack root dir prefix", interactive=True, visible=config.tag_mode)
                tag_json = load_tag_json()
                NPCs_can_download_ = gr.CheckboxGroup(
                    choices=sorted(tag_json.keys()),
                    label='choose NPCs',
                    interactive=True,
                    visible=config.tag_mode)
                pack_tagged_images_ = gr.Button("Pack tagged NPCs to .zip", visible=config.tag_mode, interactive=False)
        for folder_NPC in tqdm(folder_NPCs, desc="Loading folder_NPC"):
            folder_nums = os.listdir(os.path.join(config.img_root_path, folder_NPC))
            folder_nums = sorted([folder_num.zfill(4) for folder_num in folder_nums if folder_num.split('.')[-1] not in ['json']])
            with open(os.path.join(config.img_root_path, folder_NPC, f"{folder_NPC}.json"), 'r') as f:
                folder_NPC_json = json.load(f)
            folder_nums = [folder_num.lstrip('0') for folder_num in folder_nums]
            folder_nums = ['0' if folder_num == '' else folder_num for folder_num in folder_nums]
            with gr.Group():
                with gr.Row():
                    folder_NPC_ = gr.Label(folder_NPC, label="folder_NPC")
                with gr.Accordion("", open=False):
                    for folder_num in tqdm(folder_nums, desc="Loading folder_num"):
                        card_type = folder_NPC_json["output_image_list"][folder_num]["json_data"]["card_type"]
                        card_name = config.card_type_name_dict[card_type]
                        prompts = folder_NPC_json["output_image_list"][folder_num]["prompts"]
                        folder_num_path_s, tag_s, note_s, image_path_s, image_tag_s, image_num_s = create_item(folder_NPC, folder_num, card_name, prompts)
                        folder_num_path_list.extend(folder_num_path_s)
                        tag_list.extend(tag_s)
                        note_list.extend(note_s)
                        image_path_list.extend(image_path_s)
                        image_tag_list.extend(image_tag_s)
                        image_num_list.extend(image_num_s)

        save_tag_json_.click(
            fn=save_tag_json,
            inputs=folder_num_path_list+tag_list+note_list+image_path_list+image_tag_list+image_num_list,
            outputs=[status_, NPCs_can_download_]
        )
        pack_tagged_images_.click(
            fn=pack_tagged_images,
            inputs=[pack_root_dir_prefix_, NPCs_can_download_],
            outputs=[status_]
        )
