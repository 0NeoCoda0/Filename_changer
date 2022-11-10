import os
import shutil

dirlist = os.listdir()
destination = os.getcwd()
for dir in dirlist:
    if os.path.isdir(dir):
        file_list_inside = os.listdir(dir)
        for filename in file_list_inside:
            source_path = f"{destination}\{dir}\{filename}"
            if os.path.exists(source_path):  
                shutil.move(source_path, destination)