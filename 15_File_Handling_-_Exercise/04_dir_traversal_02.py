import os
import re


def save_extensions(dir_name):
    ext_list = {}
    for filename in os.listdir(dir_name):
        if os.path.isdir(f'{dir_name}/{filename}'):  # file = os.path.join(dir_name, filename)
            pass

        else:
            pattern = r'(\.{1}[a-z]+)'
            ext = re.findall(pattern, filename)[0]
            if ext not in ext_list:
                ext_list[ext] = []
            ext_list[ext].append(filename)
