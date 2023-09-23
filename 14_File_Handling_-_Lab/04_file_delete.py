"""
Create a program that deletes the file you created in the previous task. If you try to delete the file multiple times,
print the message: 'File already deleted!'
"""
import os.path

cur_dir = os.path.dirname(__file__)
file_name = '03_my_first_file.txt'
file_path = os.path.abspath(os.path.join(cur_dir, file_name))


try:
    os.remove(file_path)
    print('File deleted')
except FileNotFoundError:
    print('File Not Found')