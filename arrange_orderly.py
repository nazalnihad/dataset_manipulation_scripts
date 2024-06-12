import os

def rename_files(image_folder, label_folder):
    #  all image and label files
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg')]) 
    label_files = sorted([f for f in os.listdir(label_folder) if f.endswith('.txt')])
    # print(image_files[:10])
    # print(label_files[:10])

    if len(image_files) != len(label_files):
        print("The number of images and labels do not match.")
        return

    for idx, (img_file, label_file) in enumerate(zip(image_files, label_files)):
        new_img_name = f"IP{idx + 1}.jpg"  # Change the extension as needed
        new_label_name = f"IP{idx + 1}.txt"
        
        os.rename(os.path.join(image_folder, img_file), os.path.join(image_folder, new_img_name))
        os.rename(os.path.join(label_folder, label_file), os.path.join(label_folder, new_label_name))

image_folder = 'data_prep/images'
label_folder = 'data_prep/labels'
rename_files(image_folder, label_folder)
