import zipfile
import os

def zip_directory(directory, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory))

# Specify the directory you want to zip
directory_to_zip = 'backup_data/final/data'

# Specify the name of the zip file
zip_filename = 'data.zip'

# Call the function to create the zip file
zip_directory(directory_to_zip, zip_filename)

print(f'Zip file "{zip_filename}" created successfully.')
