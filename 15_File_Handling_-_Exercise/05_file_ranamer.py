import os

directory = input('Enter target directory: ')
old_string = input('Enter string to replace: ')
new_string = input('Enter new string: ')

files_in_dir = os.listdir(directory)

for file_name in files_in_dir:
    file_path = f"{directory}/{file_name}"
    if os.path.isfile(file_path):
        new_name = file_name.replace(old_string, new_string)
        new_path = f"{directory}/{new_name}"
        os.rename(file_path, new_path)
