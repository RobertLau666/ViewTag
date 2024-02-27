import os

port = 12401
default_pack_root_dir_prefix = "output/pack_tagged_images"


######## MGC
# # 2024.2.19: MGC生图，就是看一下风格的效果
# project_root_dir = "/dfs/comicai/chenyu.liu/ugc_generate_sample"
# NPCs_folder_name = "MGC_images"
# output_images_dir = f"output_images/{NPCs_folder_name}"
# img_root_path = os.path.join(project_root_dir, output_images_dir)
# appointed_NPC_names = []
# tag_json_file_path = f"output/json/{NPCs_folder_name}_tag.json"
# tag_txt_file_path = f"output/txt/{NPCs_folder_name}_tag.txt"
# tag_mode = True
# # # record:
# # port = 12403

# # 2024.2.2: MGC生图，就是看一下风格的效果
# project_root_dir = "/dfs/comicai/chenyu.liu/ugc_generate_sample"
# NPCs_folder_name = "MGC_images"
# output_images_dir = f"output_images/{NPCs_folder_name}"
# img_root_path = os.path.join(project_root_dir, output_images_dir)
# appointed_NPC_names = []
# tag_json_file_path = f"output/json/{NPCs_folder_name}_tag.json"
# tag_txt_file_path = f"output/txt/{NPCs_folder_name}_tag.txt"
# tag_mode = False
# # record:
# port = 12403


######## wishwell
# 2024.2.2 离线60-1/854@张意邈
# project_root_dir = "/dfs/comicai/chenyu.liu/ugc_generate_sample"
# NPCs_folder_name = "wishwell_images"
# output_images_dir = f"output_images/{NPCs_folder_name}"
# img_root_path = os.path.join(project_root_dir, output_images_dir)
# appointed_NPC_names = ['10180', '10241']
# tag_json_file_path = f"output/json/{NPCs_folder_name}_tag.json"
# tag_txt_file_path = f"output/txt/{NPCs_folder_name}_tag.txt"
# tag_mode = True
# record:
# # batch1 2024.2.4 14:15
# # 2: port = 12403 ['10003', '10022']
# # 2: port = 12404 ['10180', '10241']


######## offline_generate
# # 2024.2.2 离线60-1/854@张意邈
# project_root_dir = "/dfs/comicai/chenyu.liu/ugc_generate_sample"
# NPCs_folder_name = "ugc_NPC_images"
# output_images_dir = f"output_images/{NPCs_folder_name}"
# img_root_path = os.path.join(project_root_dir, output_images_dir)
# appointed_NPC_names = ['10002', '10020', '10030', '10039', '10044', '10049', '10063', '10071', '10077', '10082', '10084', '10093', '10098', '10099', '10122', '10126', '10131', '10136', '10142', '10169', '10439', '10476', '10910', '10959', '10960', '10971', '10974', '10986', '10988', '11021']
# tag_json_file_path = f"output/json/{NPCs_folder_name}_tag.json"
# tag_txt_file_path = f"output/txt/{NPCs_folder_name}_tag.txt"
# tag_mode = True
# # record:
# # batch1 2024.2.2 15:12
# # 60: ['10002', '10020', '10030', '10039', '10044', '10049', '10063', '10071', '10077', '10082', '10084', '10093', '10098', '10099', '10122', '10126', '10131', '10136', '10142', '10169', '10439', '10476', '10910', '10959', '10960', '10971', '10974', '10986', '10988', '11021', '11033', '11052', '11063', '11065', '11087', '11088', '11095', '11105', '11143', '11150', '11156', '11900', '12986', '13365', '13433', '13450', '13458', '13461', '13467', '13477', '13487', '13490', '13496', '13531', '13560', '13565', '13596', '13599', '13611', '13624']
# # 30: port = 12401 ['10002', '10020', '10030', '10039', '10044', '10049', '10063', '10071', '10077', '10082', '10084', '10093', '10098', '10099', '10122', '10126', '10131', '10136', '10142', '10169', '10439', '10476', '10910', '10959', '10960', '10971', '10974', '10986', '10988', '11021']
# # 30: port = 12402 ['11033', '11052', '11063', '11065', '11087', '11088', '11095', '11105', '11143', '11150', '11156', '11900', '12986', '13365', '13433', '13450', '13458', '13461', '13467', '13477', '13487', '13490', '13496', '13531', '13560', '13565', '13596', '13599', '13611', '13624']


# # 2024.1.29 看一下修改tags后的效果，不需要打标@张意邈
# project_root_dir = "/dfs/comicai/chenyu.liu/ugc_generate_sample"
# NPCs_folder_name = "ugc_NPC_images"
# output_images_dir = f"output_images/{NPCs_folder_name}"
# img_root_path = os.path.join(project_root_dir, output_images_dir)
# appointed_NPC_names = []
# tag_json_file_path = f"output/json/{NPCs_folder_name}_tag.json"
# tag_txt_file_path = f"output/txt/{NPCs_folder_name}_tag.txt"
# tag_mode = False

# project_root_dir = "/dfs/comicai/chenyu.liu/ugc_generate_sample"
# NPCs_folder_name = "test_imgs_2"
# output_images_dir = f"output_images/{NPCs_folder_name}"
# img_root_path = os.path.join(project_root_dir, output_images_dir)
# appointed_NPC_names = ['9939']
# tag_json_file_path = f"output/json/{NPCs_folder_name}_tag.json"
# tag_txt_file_path = f"output/txt/{NPCs_folder_name}_tag.txt"
# tag_mode = False

######## test
img_root_path = "/dfs/comicai/chenyu.liu/others/show_url_imgs_gradio/test_show_images"
appointed_NPC_names = ['10002', '10439']
tag_json_file_path = f"output/json/{img_root_path.split('/')[-1]}_tag.json"
tag_txt_file_path = f"output/txt/{img_root_path.split('/')[-1]}_tag.txt"
tag_mode = True

# img_root_path = "/dfs/comicai/chenyu.liu/ugc_generate_sample/output_offline_card_NPC"
# folder_NPCs_to_tag = ['2814749767106572', '2814749767106590', '9939']
# tag_json_file_path = f"output/json/{img_root_path.split('/')[-1]}_tag.json"
# tag_txt_file_path = f"output/txt/{img_root_path.split('/')[-1]}_tag.txt"
# tag_mode = True


### record
## all NPCs: 
# '10003' '11680', '13531', '14388', '21414', '21738', '21873', '2814749767106572', '2814749767106590', '9939'

##tmux session      port      NPC
# done:
# show_url_imgs     8003     '10003' '11680', '13531'
# show_url_imgs     8007     '14388', '21414'
# show_url_imgs_1   12401    '21738', '21873'
# show_url_imgs     12402    '2814749767106572', '2814749767106590', '9939'
# launched and tagging:
# launching:
# not yet launched:
