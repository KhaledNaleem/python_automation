import shutil
import os

# Walking through the folder tree
for folders,subfolders,filenames in os.walk('/home/USER'):
    for filename in filenames:
        if filename.endswith('.jpg'):
            shutil.move(filename, '/home/USER/MY_IMAGES')
        elif filename.endswith('.pdf'):
            shutil.move(filename, '/home/USER/MY_FILES')
        elif filename.endswith('.exe'):
            shutil.move(filename, '/home/USER/MY_SOFTWARES')
        break