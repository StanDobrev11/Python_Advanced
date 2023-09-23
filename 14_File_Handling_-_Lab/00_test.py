import os

# file = open('text.txt', 'r')

# content = file.read()
# content = file.readlines()
# content = file.readline()


# abs_path = os.path.abspath('')


# print(type(abs_path))


# abs_path = os.path.abspath('text.txt')  # provides full path to file in current directory
# print(__file__)  # provides full path to file in current directory
# print(abs_path)

# print(os.path.join(abs_path, 'text.txt'))

# print(os.path.dirname(abs_path))  # gives current file directory

# print(os.path.dirname(__file__))
# file = open(os.path.join(os.path.dirname(__file__), 'test_dir', 'cars.txt'), 'r')
# print(file.read())

# try:
#     file = open(os.path.join(os.path.dirname(__file__), 'test_dir', 'trucks.txt'), 'r')
#     print(file.read())
# except FileNotFoundError:
#     print('File Not Found')
# else: # not finally because file not defined
#     file.close()

# file = open(os.path.join(os.path.dirname(__file__), 'test_dir', 'new_test.txt'), 'x')
# file.write('I wanna be a Python MASTER\nYou may try!!\nTry again\n')
# file.close()
# file = open(os.path.join(os.path.dirname(__file__), 'test_dir', 'new_test.txt'), 'r')
# # print(file.read())
# file.close()
# file = open(os.path.join(os.path.dirname(__file__), 'test_dir', 'new_test.txt'), 'a')
# file.write('I want it ALL\n')
# # file.close()
# file = open(os.path.join(os.path.dirname(__file__), 'test_dir', 'new_test.txt'), 'r')
# print(file.read())
# file.close()

# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'api.env')))

txt = ['-I', 'was', 'quick', 'to', 'judge', 'him,', 'but', 'it', "wasn't", 'his', 'fault.\n-Is', 'this', 'some', 'kind', 'of', 'joke?!', 'Is', 'it?\n-Quick,', 'hide', 'here…It', 'is', 'safer.\n']
