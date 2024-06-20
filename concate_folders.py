import os
import shutil

def gather_images(src_root, dst_folder):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
        print(f"Created directory {dst_folder}")

    for root, dirs, files in os.walk(src_root):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', 'jpeg')):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_folder, file)
                print(f"Copying {src_file} to {dst_file}")
                shutil.copy(src_file, dst_file)

src_root = 'C:/Users/nazal/Downloads/n'
dst_folder = "C:/Users/nazal/Downloads/hg_data"

gather_images(src_root, dst_folder)
