# show_tag_imgs
This is an showing and tagging image implementation project in gradio version, for a specific directory structure of the image folder.

The images folder struction is similar to the following:
```
| test_images/
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
    > **```display_mode```**: ```1``` or ```2```, which indicates that how many folders between ```img_root_path``` and the images location.

    > **```img_root_path```**: if ```display_mode``` is ```1```, indicates there is 1 folders between ```img_root_path``` (such as ```"test_images/10002/"```) and the images location; if ```display_mode``` is ```2```, indicates there are 2 folders between ```img_root_path``` (such as ```"test_images/"```) and the images location.

    > **```tag_mode```**: in addition to showing, whether tagging is required.

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
| ```display_mode = 1``` <br> ```img_root_path = "test_images/10002/"``` | ```display_mode = 2``` <br> ```img_root_path = "test_images/"``` |
| ------- | ------- |
| ![demo_1.jpeg](images/demo_images/demo_1.jpeg)  | ![demo_2.jpeg](images/demo_images/demo_2.jpeg) |