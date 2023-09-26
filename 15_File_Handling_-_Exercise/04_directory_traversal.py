"""
Write a program that traverses a given directory for all files. Search through the first level of the directory only and
write information about each found file in report.txt. The files should be grouped by their extension. Extensions
should be ordered by name alphabetically. The files with extensions should also be sorted by name. report.txt should
be saved in the chosen directory.

"""
import os
import re


def get_filepath(filename):
    return f"txt_files/{filename}"


def write_(filename, data):
    with open(filename, 'w') as file:
        file.write(data)


def get_file_list(tgt_dir):
    path = tgt_dir
    root_dir = {tgt_dir: []}
    all_files = {}
    file_list = os.listdir(tgt_dir)  # a list with the directory content
    pattern = r'(\.{1}[a-z]+)'
    for file in file_list:
        try:
            ext = re.findall(pattern, file)[0]
            if ext not in all_files:
                all_files[ext] = []
            all_files[ext].append(file)
        except IndexError:
            all_files[file] = get_file_list(path + '/' + file)

    root_dir[tgt_dir] = all_files
    return root_dir


def get_data_as_str(ext_dct):
    data = ''
    for k, v in sorted(ext_dct.items(), key=lambda x: x[0]):
        data += f'{k}\n'
        for value in sorted(v):
            data += f'- - - {value}\n'

    return data


target_dir = 'TXT_FILES'

dirs = get_file_list(target_dir)
result_data = get_data_as_str(dirs)
write_('report.txt', result_data)
