"""
Write a program that reads a list of words from the file words.txt and finds how many times each of the words is
contained in another file text.txt. Matching should be case-insensitive.
The results should be written into other text files. Sort the words by frequency in descending order.

words.txt           input.txt           output.txt
quick is fault
                    '''-I was quick to judge him, but it wasn't his fault.
                    -Is this some kind of joke?! Is it?
                    -Quick, hide here…It is safer.'''
                                        is - 3
                                        quick - 2
                                        fault - 1
"""
import os.path


def get_file_path(filename):
    cur_dir = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(cur_dir, filename))


def create_file(filename, *args):
    try:
        with open(get_file_path(filename), 'x') as f:
            f.writelines(args)
            print('File created')
    except FileExistsError:
        print('FileExists')


def delete_file(filename):
    try:
        os.remove(get_file_path(filename))
        print('File deleted')
    except FileNotFoundError:
        print('FileNotFound')


def get_text_as_list(filename):
    try:
        with open(get_file_path(filename), 'r') as f:
            text = f.read().split(' ')
            return text
    except FileNotFoundError:
        print('FileNotFound')


def read_file(filename):
    try:
        with open(get_file_path(filename), 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print('FileNotFound')


def write_to_file(filename, text):
    try:
        with open(get_file_path(filename), 'a') as f:
            f.write(text)
    except FileNotFoundError:
        print('FileNotFound')


# delete_file('words.txt')
# delete_file('input.txt')
delete_file('output.txt')


# create_file('words.txt', 'quick is fault')

# create_file(
#     'input.txt',
#     """-I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here…It is safer.
# """
# )

target_words = get_text_as_list('words.txt')
target_text = get_text_as_list('input.txt')

create_file('output.txt', '')
for word in target_words:
    count = target_text.count(word)
    write_to_file('output.txt', f'{word} - {count}\n')

read_file('output.txt')

