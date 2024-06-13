import os
import shutil

def gather_images(src_root, dst_folder):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
        print(f"Created directory {dst_folder}")

    for root, dirs, files in os.walk(src_root):
        for file in files:
            # Check if the file is an image (you can add more extensions if needed)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff','.txt')):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_folder, file)
                print(f"Copying {src_file} to {dst_file}")
                shutil.copy(src_file, dst_file)

src_root = 'D:/projects/iist/backup_data/final/f_data/labels'
dst_folder = "D:/projects/iist/backup_data/final/c_data"

gather_images(src_root, dst_folder)
