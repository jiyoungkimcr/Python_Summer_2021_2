import os
folder = 'documents'

def sum_space(folder):
    sum_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            sum_size += os.path.getsize(file_path)
    return sum_size

my_folder = "/Users/jiyoungkim/Desktop/python_20212"
print("Total size is:" + str(sum_space(my_folder)) + "byte")

