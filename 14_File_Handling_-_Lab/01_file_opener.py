"""
You are given a file called 01_text.txt with the following text:

#This is some random line
#This is the second line
#And this is the third one

Create a program that opens the file. If the file is found, print 'File found'. If the file is not found, print 'File
not found'.
"""
import os.path

cur_dir = os.path.dirname(__file__)

# file = open(os.path.abspath(os.path.join(cur_dir, '01_text.txt')), 'a+')
# file.write('This is some random line\nThis is the second line\nAnd this is the third one\n')
# file.close()

# file = open(os.path.abspath(os.path.join(cur_dir, '01_text.txt')))
if os.path.isfile(os.path.abspath(os.path.join(cur_dir, '01_text.txt'))):
    print('File found')
else:
    print('File Not Found')
