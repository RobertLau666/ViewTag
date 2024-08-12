import os


port = 12402
# view_mode = 1
# img_root_path = "images/test_images/10002"
view_mode = 2
img_root_path = "images/test_images"
tag_mode = True
appointed_NPC_names = []


if view_mode == 1:
    tag_json_file_path = f"output/json/{img_root_path.split('/output_')[-1].replace('/','_')}_tag.json"
    tag_txt_file_path = f"output/txt/{img_root_path.split('/output_')[-1].replace('/','_')}_tag.txt"
elif view_mode == 2:
    card_type_name_dict = {
        "1": "梦境卡",
        "2": "事件卡",
        "3": "心动卡"
    }
    mode = "test"
    if mode in ["MGC", "wishwell", "chat"]:
        round_num = "2"
        project_root_dir = "/dfs/comicai/chenyu.liu/ugc_generate_sample"
        NPCs_folder_name = f"{mode}_images_{round_num}"
        output_images_dir = f"output_images/{NPCs_folder_name}"
        img_root_path = os.path.join(project_root_dir, output_images_dir)
        tag_json_file_path = f"output/json/{NPCs_folder_name}_tag.json"
        tag_txt_file_path = f"output/txt/{NPCs_folder_name}_tag.txt"
    elif mode in ["test"]:
        tag_json_file_path = f"output/json/{img_root_path.split('/')[-1]}_tag.json"
        tag_txt_file_path = f"output/txt/{img_root_path.split('/')[-1]}_tag.txt"