import os
import json
from datetime import datetime
from configs import config


def get_current_time():
    current_time = datetime.now()
    date_suffix = current_time.strftime("_%Y%m%d")
    time_suffix = current_time.strftime("_%H%M%S")

    return '_time' + date_suffix + time_suffix

def list_files(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)

    return sorted(all_files)

def create_dir_or_file(path):
    if not os.path.exists(path):
        file_name, file_extension = os.path.splitext(path)
        print("file_name, file_extension",file_name, file_extension)
        if file_extension == "":
            os.makedirs(path, exist_ok=True)
        else:
            if not os.path.exists(path):
                with open(path, 'w') as file:
                    file.write('{}') # it is json format here in this project
                
def load_tag_json():
    if config.tag_mode:
        create_dir_or_file(config.tag_json_file_path)
        with open(config.tag_json_file_path, 'r') as f:
            tag_json = json.load(f)
    else:
        tag_json = {}

    return tag_json

def chunk_list(input_list, chunk_num):
    chunk_size = len(input_list) // chunk_num
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

def save_tag_txt():
    tag_json = load_tag_json()
    good_images_num, all_images_num = 0, 0
    tag_txt_list = []

    for NPC_id, NPC_tag_dict in tag_json.items():
        for NPC_group, NPC_group_dict in NPC_tag_dict.items():
            all_images_num += len(NPC_group_dict["tags_"])
            if NPC_group_dict["tag"] == 0:
                for img_path, tag in NPC_group_dict["tags_"].items():
                    if tag == 0:
                        tag_txt_list.append(img_path)
                        good_images_num += 1

    with open(config.tag_txt_file_path, "w") as file:
        for item in tag_txt_list:
            file.write(item + '\n')
    
    return good_images_num, all_images_num