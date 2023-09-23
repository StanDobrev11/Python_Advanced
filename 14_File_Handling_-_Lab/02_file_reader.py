"""
You are given a file called 02_numbers.txt with the following content:
1
2
3
4
5

Create a program that reads the numbers from the file. Print on the console the sum of those numbers.
"""
import os.path

cur_dir = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(cur_dir, '02_numbers.txt'))

# file = open(file_path, 'a+')
# file.write('1\n2\n3\n4\n5\n')
# file.close()

try:
    open(file_path, 'r+')
    file = open(file_path, 'r+')
    rr = file.readlines()
    file.seek(0)
    nums = [int(x) for x in file.readlines()]
    print(nums)
    sum_nums = sum(nums)
    print(sum_nums)
    print(rr)
    file.close()
except FileNotFoundError:
    print('File not found')

