'''
/Users/jiyoungkim/Desktop/python_20212/
'''
import os
import os.path
from pip._vendor.distlib.compat import raw_input

print('Please provide the path of the folder you want to know the Space (Put the slash at the end):')
path = raw_input()
count = 0


''' Counts the number of files in a directory '''
def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1

    return count


# The following line prints the number of files in the current directory:
print(fcount(path))
print(os.listdir(path))