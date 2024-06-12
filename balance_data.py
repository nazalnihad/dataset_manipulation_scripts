import os

def remove_unmatched_labels(image_folder, label_folder):
    # List all image and label files
    image_files = {os.path.splitext(f)[0] for f in os.listdir(image_folder) if f.endswith('.jpg')}  # Change the extension as needed
    label_files = {os.path.splitext(f)[0] for f in os.listdir(label_folder) if f.endswith('.txt')}

    # Find label files without a corresponding image file
    unmatched_images = image_files-label_files 

    for label in unmatched_images:
        os.remove(os.path.join(image_folder, f"{label}.jpg"))

    print(f"Removed {len(unmatched_images)} unmatched label files.")

image_folder = 'D:/projects/iist/backup_data/final_data/predictions/data/val/images'
label_folder = 'D:/projects/iist/backup_data/final_data/predictions/data/val/labels'
remove_unmatched_labels(image_folder, label_folder)
