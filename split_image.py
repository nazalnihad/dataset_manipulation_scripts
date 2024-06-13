import os
from PIL import Image
import shutil
import random

def split_image(image_path, prefix, index, output_path):
    try:
        # Open an image file
        with Image.open(image_path) as img:
            # Get dimensions
            width, height = img.size
            print(f"Processing image: {image_path} with size {width}x{height}")
            
            # Calculate half dimensions
            half_width = width // 2
            half_height = height // 2
            
            # Define box coordinates for each quadrant
            boxes = [
                (0, 0, half_width, half_height),            # top-left
                (half_width, 0, width, half_height),        # top-right
                (0, half_height, half_width, height),       # bottom-left
                (half_width, half_height, width, height)    # bottom-right
            ]
            
            # Split and save each quadrant
            for i, box in enumerate(boxes):
                quadrant = img.crop(box)
                quadrant_path = os.path.join(output_path, f"{prefix}_{index * 4 + i}.jpg")
                quadrant.save(quadrant_path)
                print(f"Saved quadrant {i} to {quadrant_path}")
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")

def process_images(from_path, to_path, prefix, num_images):
    try:
        images = os.listdir(from_path)
        print(f"Found {len(images)} images in {from_path}")
        
        random.shuffle(images)
        selected_images = images[:num_images]
        print(f"Selected {num_images} images for processing")
        
        if not os.path.exists(to_path):
            os.makedirs(to_path)
            print(f"Created directory {to_path}")
        
        for index, image in enumerate(selected_images):
            image_path = os.path.join(from_path, image)
            print(f"Processing image {index + 1}/{num_images}: {image_path}")
            split_image(image_path, prefix, index, to_path)
        
        print(f"Processing complete. {num_images * 4} images saved to {to_path}")
    except Exception as e:
        print(f"Error during processing: {e}")

# paths and parameters
from_path = 'C:/Users/nazal/Downloads/not_pest/random_noise'
to_path = 'D:/projects/iist/classification/data/not_pest'
prefix = 'RAN'
num_images = 2000

process_images(from_path, to_path, prefix, num_images)
