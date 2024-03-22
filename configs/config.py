import os

port = 12401
default_pack_root_dir_prefix = "output/pack_tagged_images"

mode = "wishwell"
round_num = "2"
appointed_NPC_names = ["10831", "2533274790467305", "2533274790612038", "2533274790644859"]
tag_mode = False

if mode in ["MGC", "wishwell", "chat"]:
    project_root_dir = "/dfs/comicai/chenyu.liu/ugc_generate_sample"
    NPCs_folder_name = f"{mode}_images_{round_num}"
    output_images_dir = f"output_images/{NPCs_folder_name}"
    img_root_path = os.path.join(project_root_dir, output_images_dir)
    tag_json_file_path = f"output/json/{NPCs_folder_name}_tag.json"
    tag_txt_file_path = f"output/txt/{NPCs_folder_name}_tag.txt"

elif mode in ["test"]:
    img_root_path = "/dfs/comicai/chenyu.liu/others/show_url_imgs_gradio/test_show_images"
    tag_json_file_path = f"output/json/{img_root_path.split('/')[-1]}_tag.json"
    tag_txt_file_path = f"output/txt/{img_root_path.split('/')[-1]}_tag.txt"
