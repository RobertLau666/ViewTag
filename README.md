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
Modify parameters in configs/config.py
```
python show_url_imgs_app.py
```
Then you can open link in local: http://0.0.0.0:[port], for example: http://0.0.0.0:12400; Or open it in the following way: [HostName]:[port], for example: 192.168.190.60:12400

Tagging rules:
- The checkbox "bad" under each group of images is selected to represent the whole group of bad images
- The checkbox "bad" under each image is selected to represent that a single image is a bad image, if you want select only 1 good image in 3 images, you need to tag two "bad" in each group, and leave one without "bad" as the good image to keep
- Click the "save tag json" button to temporarily save or save, and a json file containing the tagging information of each image and a txt file containing paths of good images picked out
- Check the NPCs you want to pack
- Clicking the "Pack tagged NPCs to.zip" button to pack all the good images into a.zip file according to the original image structure, but this step is not necessary, getting json file is enough

## Result presentation
![demo.jpeg](demo_images/demo.jpeg)
