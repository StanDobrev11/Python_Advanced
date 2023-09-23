"""
Create a program that creates a file called my_first_file.txt. In that file, write a single line with the content:
'I just created my first file!'
"""

import os.path

cur_dir = os.path.dirname(__file__)
file_name = '03_my_first_file.txt'
file_path = os.path.abspath(os.path.join(cur_dir, file_name))

try:
    file = open(file_path, 'x')
    file.write('I just created my first file!\n')
    print('File created')
    file.close()
except FileExistsError:
    print('File already created')
