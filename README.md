# show_tag_imgs
This is an showing and tagging image implementation project in gradio version, for a specific directory structure of the image folder.

The images folder struction is similar to the following:
```
| test_show_images/
|---- 10002/
|-------- 0/
|------------ 10002_0_0.png
|------------ 10002_0_1.png
|------------ ...
|-------- 1/
|------------ 10002_1_0.png
|------------ 10002_1_1.png
|------------ ...
|-------- ...
|-------- 10002.json
|---- ...
```

## Usage
1. Modify parameters in ```configs/config.py```
    > **```display_mode```**: ```1``` or ```2```, which respectively indicates showing images containing level-1 directory or level-2 directory.

    > **```img_root_path```**: if ```display_mode``` is ```1```, this value is a level-1 directory, such as ```"test_show_images/"```; if ```display_mode``` is ```2```, this value is a level-2 directory, such as ```"test_show_images/10002/"```.

    > **```tag_mode```**: in addition to show, whether tagging is required.

    > **```appointed_NPC_names```**: ```[]``` by default, all images in ```img_root_path``` are showed, if this parameter is not ```[]```, the appointed images are showed.

2. Run
    ```
    python app.py
    ```
    Please wait patiently for the images to load, then open link in local: ```http://0.0.0.0:[port]```, for example: ```http://0.0.0.0:12400```; or open it in the following way: ```[HostName]:[port]```, for example: ```192.168.190.60:12400```.
    
    > **Tagging rules:**
    > - The checkbox ```bad``` under each group of images is selected to represent the whole group of bad images.
    > - The checkbox ```bad``` under each image is selected to represent that a single image is a bad image, if you want select only 1 good image in 3 images, you need to tag two ```bad``` in each group, and leave one without ```bad``` as the good image to keep.
    > - If necessary, write a note in the ```note```.
    > - Click the ```Save tag json``` button to temporarily save or save, and a ```.json``` file containing the tagging information of each image and a ```.txt``` file containing paths of good images will be generated.
    > - Check the NPCs you want to pack, click the ```Pack tagged NPCs to .zip``` button to pack all the good images into a ```.zip``` file according to the original image structure, but this step is not necessary, getting ```.json``` file is enough.

## Result presentation
| ```display_mode = 1``` <br> ```img_root_path = "test_show_images/"``` | ```display_mode = 2``` <br> ```img_root_path = "test_show_images/10002/"``` |
| ------- | ------- |
| ![demo.jpeg](demo_images/demo.jpeg)  | ![demo_2.jpeg](demo_images/demo_2.jpeg) |