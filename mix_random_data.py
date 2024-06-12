import os
import shutil

def add_data(current_img_path, current_label_path, new_img_path, new_label_path, prefix='EV', interval=2):
    current_img_files = set(os.listdir(current_img_path))
    current_label_files = set(os.listdir(current_label_path))

    new_img_files = os.listdir(new_img_path)
    new_label_files = os.listdir(new_label_path)

    next_index = 1

    for i in range(0, len(new_img_files), interval):
        img_file = new_img_files[i]
        label_file = os.path.splitext(img_file)[0] + '.txt'

        if label_file not in new_label_files:
            print(f"Skipping {img_file} as the corresponding label file is missing.")
            continue

        new_img_name = f"{prefix}{next_index}.{os.path.splitext(img_file)[1][1:]}"
        new_label_name = f"{prefix}{next_index}.txt"

        if new_img_name not in current_img_files and new_label_name not in current_label_files:
            shutil.copy(os.path.join(new_img_path, img_file), os.path.join(current_img_path, new_img_name))
            shutil.copy(os.path.join(new_label_path, label_file), os.path.join(current_label_path, new_label_name))
            print(f"Copied {img_file} and {label_file} to {new_img_name} and {new_label_name} in the current directories.")
            next_index += 1

current_img_path = 'D:/projects/iist/backup_data/final_data/predictions/data/val/images'
current_label_path = 'D:/projects/iist/backup_data/final_data/predictions/data/val/labels'
new_img_path = 'D:/projects/iist/backup_data/final/data/images/train'
new_label_path = 'D:/projects/iist/backup_data/final/data/labels/train'

add_data(new_img_path,new_label_path,current_img_path,current_label_path )