import os
from PIL import Image

# File Paths
script_path = os.path.dirname(os.path.abspath(__file__))
raw_img_dir = r'\img\raw'
resized_img_dir = r'\img\resized'

# Check If Raw Image Folder For Image Files
for file in os.listdir(script_path+raw_img_dir):
    if file.lower().endswith(('.png','.jpg','.jpeg')):
        # Scaling Image To Lower Resolution (Maintains Aspect Ratio)
        s = 0.2 # Scale Factor
        image = Image.open(script_path+raw_img_dir+r'\\'+file)
        new_image = image.resize((int(image.size[0]*s),int(image.size[1]*s)))
        new_image.save(script_path+resized_img_dir+r'\\'+file)