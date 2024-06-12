import os
import shutil
import random

def create_test_data(image_source_dir, label_source_dir, dest_dir, num_files):
    # Create destination directories if they don't exist
    images_dest = os.path.join(dest_dir, 'images')
    labels_dest = os.path.join(dest_dir, 'labels')
    os.makedirs(images_dest, exist_ok=True)
    os.makedirs(labels_dest, exist_ok=True)

    # Get list of all images in the source directory
    all_images = [f for f in os.listdir(image_source_dir) if f.endswith(('.jpg', '.png'))]
    
    # Randomly select the specified number of images
    selected_images = random.sample(all_images, min(num_files, len(all_images)))
    
    # Copy each selected image and its corresponding label
    for image_name in selected_images:
        image_source_path = os.path.join(image_source_dir, image_name)
        
        # Replace the file extension with .txt for the label file
        if image_name.endswith('.jpg'):
            label_name = image_name.replace('.jpg', '.txt')
        elif image_name.endswith('.png'):
            label_name = image_name.replace('.png', '.txt')

        label_source_path = os.path.join(label_source_dir, label_name)
        
        if os.path.exists(label_source_path):
            shutil.copy(image_source_path, images_dest)
            shutil.copy(label_source_path, labels_dest)
        else:
            print(f"Warning: Label {label_name} for image {image_name} does not exist in the label source directory.")

# Example usage:
image_source_dir = 'backup_data/final/data/images/train'  # Change this to the path of your source images folder
label_source_dir = 'backup_data/final/data/labels/train'  # Change this to the path of your source labels folder
dest_dir = 'backup_data/final/test_data'  # Change this to the path where you want to create the new test data folder
num_files = 2000  # Change this to the number of files you want to select

create_test_data(image_source_dir, label_source_dir, dest_dir, num_files)
