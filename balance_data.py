import os

def remove_unmatched_images(image_folder, label_folder):
    # List all image files with .jpg and .png extensions
    image_files = {os.path.splitext(f)[0] for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.png'))}
    # List all label files with .txt extension
    label_files = {os.path.splitext(f)[0] for f in os.listdir(label_folder) if f.endswith('.txt')}

    # Find image files without a corresponding label file
    unmatched_images = image_files - label_files

    # Remove unmatched .jpg images
    for image in unmatched_images:
        jpg_image_path = os.path.join(image_folder, f"{image}.jpg")
        if os.path.exists(jpg_image_path):
            os.remove(jpg_image_path)
            print(f"Removed {jpg_image_path}")

    # Remove unmatched .png images
    for image in unmatched_images:
        png_image_path = os.path.join(image_folder, f"{image}.jpeg")
        if os.path.exists(png_image_path):
            os.remove(png_image_path)
            print(f"Removed {png_image_path}")

    print(f"Removed {len(unmatched_images)} unmatched image files.")
# Define the image and label folder paths
image_folder = 'C:/Users/nazal/Downloads/hg_data'
label_folder = "C:/Users/nazal/Downloads/hg_data"

# Run the function to remove unmatched images
remove_unmatched_images(image_folder, label_folder)
