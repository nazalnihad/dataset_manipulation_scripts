import os

def remove_files(path,extension='txt'):
    files = os.listdir(path)
    for file in files:
        name = os.path.splitext(file)
        print(name[1][1:])
        if name[1][1:] == extension:
            os.remove(os.path.join(path,file))
            # os.remove(file)

remove_files('C:/Users/nazal/Downloads/n/test')