import os

port = 12403
display_mode = 2
img_root_path = "/data/dev-linky/as-loki-lcy-folder/show_tag_imgs/test_show_images"
img_root_path = "/data/dev-linky/as-loki-lcy-folder/show_tag_imgs/test_show_images/10002"
# img_root_path = "/data/dev-linky/as-loki-tst/background_generate_service/output_Dream_Diffusion_LIGHTNING_XL_SD_LIGHTNING_XL_V2/i2i"
tag_mode = True
appointed_NPC_names = []


if display_mode == 1:
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
        
elif display_mode == 2:
    tag_json_file_path = f"output/json/{img_root_path.split('/output_')[-1].replace('/','_')}_tag.json"
    tag_txt_file_path = f"output/txt/{img_root_path.split('/output_')[-1].replace('/','_')}_tag.txt"
