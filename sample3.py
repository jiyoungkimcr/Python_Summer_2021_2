def size_r(path):
    size = 0
    arr = os.listdir(path)
    for x in range(len(arr)):
        if os.path.isfile (path + "/" + arr[x]):
           size = size + os.stat(path + "/" + arr[x]).st_size
        else:
            path_x = path + "/" + arr[x]
            size += size_r(path_x)
    return size


import os
full_path = input("give path:")

size =size_r(full_path)

print(size)


import os

list = os.listdir(dir) # dir is your directory path
number_files = len(list)
print number_files



def sum_space(folder):
    sum_size = 0
    dir = os.listdir(folder)
    for f in range(len(dir)):
        path = folder + dir[f]
        if os.path.is_file(path):
            sum_size += os.stat(path).st_size
        else:
            sum_size += sum_space(path)
    return sum_size

print('Size of your folder is: ' + str(sum_space(folder)) + ' bytes')




number_of_files = len([item for item in os.listdir(dir) if os.path.isfile(os.path.join(dir, item))])
print(number_of_files)
print(os.listdir(dir))


for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        count += 1
print(count)