import os
import string
list = os.listdir(path=".")
names = []
count_files_lat = 0
count_big_dir = 0
count_files_without_num = 0
for name in list:
    if name not in names:
        names.append(name)
    if os.path.isfile(name) == True:
        name2 = os.path.splitext(name)[0]
        if any(map(str.isdigit, name2)) == 0:
            count_files_without_num += 1
        for symbol in name2:
            if symbol not in string.ascii_letters:
                flag = 1
            if flag == 1:
                break
        if flag != 1:
            count_files_lat += 1
        flag = 0
    if os.path.isdir(name) == True:
        name2 = ' '.join(name.split())
        words = name2.split()
        if len(words) >= 2:
            count_big_dir += 1
print(count_big_dir)
print(count_files_without_num)
print(count_files_lat)
print(names)

