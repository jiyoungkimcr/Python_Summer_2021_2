'''
/Users/jiyoungkim/Desktop/python_20212/
'''
import os
import os.path
from pip._vendor.distlib.compat import raw_input

print('Please provide the path of the folder you want to know the Space (Put the slash at the end):')
dir = raw_input()

list = os.listdir(dir)
total_number_files = len(list)
print(total_number_files)
print(list)