# show_tag_imgs
This is an image display and marking gradio implementation project, for a specific directory structure of the image folder, the images folder struction is similar to the following:
```
| test_show_images/
|---- 10002/
|-------- 0/
|------------ 10002_0_0.png
|------------ 10002_0_1.png
|------------ 10002_0_2.png
|------------ 10002_0_3.png
...
|-------- 10002.json
...

```
## Usage
Modify parameters in configs/config.py
```
python show_url_imgs_app.py
```

Tagging rules:
- The "bad" under each group of images is selected to represent the whole group of bad images
- The "bad" under each image is selected to represent that a single image is a bad image, if you want select only 1 good image in 3 images, you need to tag two "bad" in each group, and leave one without "bad" as the good image to keep
- Click the "save tag json" button to temporarily save or save, and a json file containing the tagging information of each image and a txt file containing paths of good images picked out
- Check the NPCs you want to pack
- Clicking the "Pack tagged NPCs to.zip" button to pack all the good images into a.zip file according to the original image structure

## Result presentation
![demo.jpeg](demo_images/demo.jpeg)
