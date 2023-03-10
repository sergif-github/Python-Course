#Creating a file
f = open('practice.txt', 'w+')
f.write('test')
f.close()


print("\nOs module allows us to use operating system dependent functionalities.")

import os

print("os.getcwd()", os.getcwd())
print("os.listdir()", os.listdir())

print("\nWalking though a directory")
for folder, sub_folders, files in os.walk(os.getcwd()):
    print("Currently looking at folder: " + folder)
    print("THE SUBFOLDERS ARE: ")
    for sub_fold in sub_folders:
        print("\t Subfolder: " + sub_fold)
    print("THE FILES ARE: ")
    for f in files:
        print("\t File: " + f)


import shutil

#Shutil module to to move files to different locations
#shutil.move('practice.txt', 'C:\\Users\\')
#shutil.move('C:\\Users\\practice.txt', os.getcwd())
#os.listdir()


print("\nDeleting a file")
print("os.unlink(path) deletes a file at the path your provide")
print("os.rmdir(path) deletes a folder (folder must be empty) at the path your provide")
print("hutil.rmtree(path) removes all files and folders contained in the path.")
print("Instead we will use the send2trash module. A safer alternative that sends deleted files to the trash bin")

import send2trash

send2trash.send2trash('practice.txt')
os.listdir()


