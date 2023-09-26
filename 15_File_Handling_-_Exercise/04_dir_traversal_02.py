import os
import re


def save_extensions(dir_name):
    for filename in os.listdir(dir_name):
        if os.path.isdir(f'{dir_name}/{filename}'):  # file = os.path.join(dir_name, filename)
            save_extensions(f'{dir_name}/{filename}')
        else:
            pattern = r'(\.{1}[a-z]+)'
            ext = re.findall(pattern, filename)[0]
            if ext not in file_list:
                file_list[ext] = []
            file_list[ext].append(filename)


tgt_dir = input()
file_list = {}
save_extensions(tgt_dir)

print(file_list)
