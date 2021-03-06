'''
1. Using recursion please write a function that will compute the total space occupied by a folder and its subfolders and files.
2. Please do not use os.walk or any other system command to return the size directly but implement it yourself.
3. Once you have that working correctly please add also counting of the number of files in that folder and all its subfolders
Code Writer: Jiyoung Kim
'''

import os
from pip._vendor.distlib.compat import raw_input

print('Please provide the path of the folder you want to know the Space (Put the slash at the end):')
myfolder = raw_input()

"1. Calculate total space of the folder and subfolders and files"
def sum_space(path):
    size = 0
    for f in os.scandir(path):
        if f.is_file():
            size += f.stat().st_size
        elif f.is_dir():
            size += sum_space(f.path)
    return size

print('Size of your folder is: ' + str(sum_space(myfolder)) + ' bytes')


"2. Counting the number of files in the folder and subfolders"
def fileCount(myfolder):
    count = 0
    for f in os.listdir(myfolder):
        if not f.startswith('.'): # to prevent the hidden files to be counted together
            path = os.path.join(myfolder, f)

            if os.path.isfile(path):
                count += 1

            elif os.path.isdir(path):
                count += fileCount(path)

    return count

print('Total number of files in this folder(and in subfolders) is: ' + str(fileCount(myfolder)))
