import os
import shutil
import random

def get_data(from_path, to_path, prefix='IP', num_images=15000):
    images = os.listdir(from_path)
    random.shuffle(images)
    images = images[:num_images]
    
    if not os.path.exists(to_path):
        os.makedirs(to_path)

    for i, image in enumerate(images):
        ext = os.path.splitext(image)[1]
        new_img_name = f'{prefix}{i}{ext}'
        shutil.copy(os.path.join(from_path, image), os.path.join(to_path, new_img_name))
        print(f"Copying {image} to {os.path.join(to_path, new_img_name)}")

from_path = 'C:/Users/nazal/Downloads/pestvision_data/foreground_data/Detection_IP102/JPEGImages'
to_path = 'D:/projects/iist/classification/data/pest'

get_data(from_path, to_path)
