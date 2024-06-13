import os
import random

def randomly_delete_files(folder, num_files_to_delete):
    files = [os.path.join(folder, file) for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file))]
    
    if len(files) < num_files_to_delete:
        print(f"Requested to delete {num_files_to_delete} files, but only found {len(files)} files.")
        return

    # Shuffle the list of files
    random.shuffle(files)
    

    files_to_delete = files[:num_files_to_delete]
    for file in files_to_delete:
        print(f"Deleting {file}")
        os.remove(file)

dst_folder = 'D:/projects/iist/classification/data/not_pest'
randomly_delete_files(dst_folder, 868)
