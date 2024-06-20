import os

def remove(img_path, img_label, prefix):
    image_files = sorted([f for f in os.listdir(img_path) if f.endswith(('.jpg','.jpg'))])
    label_files = sorted([f for f in os.listdir(img_label) if f.endswith('.txt')])

    for file in image_files:
        if file.startswith(prefix):
            image_path = os.path.join(img_path, file)
            label_path = os.path.join(img_label, file.replace('.jpg', '.txt'))

            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"Removed {file} from {img_path}")

            if os.path.exists(label_path):
                os.remove(label_path)
                print(f"Removed {file.replace('.jpg', '.txt')} from {img_label}")
        
remove('D:/projects/iist/backup_data/final/obj','D:/projects/iist/backup_data/final/obj','EV')