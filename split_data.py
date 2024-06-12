import os
import random
import shutil

def split_data(img_dir, label_dir, output_dir):
    # List of all image filenames (both JPG and PNG)
    img_files = sorted([f for f in os.listdir(img_dir) if f.endswith(('.jpg', '.png'))])
    
    # Shuffle randomly
    random.shuffle(img_files)
    
    total_files = len(img_files)
    train_count = int(0.8 * total_files)
    val_count = int(0.1 * total_files)
    test_count = total_files - train_count - val_count
    
    print(f'Total files: {total_files}')
    print(f'Training files: {train_count}')
    print(f'Validation files: {val_count}')
    print(f'Test files: {test_count}')
    
    # Output directories
    data_dir = os.path.join(output_dir, 'data')
    train_img_dir = os.path.join(data_dir, 'images', 'train')
    train_label_dir = os.path.join(data_dir, 'labels', 'train')
    val_img_dir = os.path.join(data_dir, 'images', 'val')
    val_label_dir = os.path.join(data_dir, 'labels', 'val')
    test_img_dir = os.path.join(data_dir, 'images', 'test')
    test_label_dir = os.path.join(data_dir, 'labels', 'test')
    os.makedirs(train_img_dir, exist_ok=True)
    os.makedirs(train_label_dir, exist_ok=True)
    os.makedirs(val_img_dir, exist_ok=True)
    os.makedirs(val_label_dir, exist_ok=True)
    os.makedirs(test_img_dir, exist_ok=True)
    os.makedirs(test_label_dir, exist_ok=True)
    
    # Copy files to respective directories
    for i, img_file in enumerate(img_files):
        label_file = os.path.splitext(img_file)[0] + '.txt'
        if i < train_count:
            shutil.copy(os.path.join(img_dir, img_file), train_img_dir)
            shutil.copy(os.path.join(label_dir, label_file), train_label_dir)
            print(f'Copying to train: {img_file} and {label_file}')
        elif i < train_count + val_count:
            shutil.copy(os.path.join(img_dir, img_file), val_img_dir)
            shutil.copy(os.path.join(label_dir, label_file), val_label_dir)
            print(f'Copying to val: {img_file} and {label_file}')
        else:
            shutil.copy(os.path.join(img_dir, img_file), test_img_dir)
            shutil.copy(os.path.join(label_dir, label_file), test_label_dir)
            print(f'Copying to test: {img_file} and {label_file}')

img_path = 'D:/projects/iist/backup_data/final/images' 
labels_path = 'D:/projects/iist/backup_data/final/labels' 
output = 'backup_data/final'
split_data(img_path, labels_path, output)
