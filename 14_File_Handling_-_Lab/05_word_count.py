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
import re


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
            return f.read()
    except FileNotFoundError:
        print('FileNotFound')


def read_file(filename):
    try:
        with open(get_file_path(filename), 'r') as f:
            return f.read()
    except FileNotFoundError:
        print('FileNotFound')


def write_to_file(filename, text):
    try:
        with open(get_file_path(filename), 'a') as f:
            f.write(text)
    except FileNotFoundError:
        print('FileNotFound')


def print_file(filename):
    try:
        with open(get_file_path(filename)) as f:
            print(f.read())
    except FileNotFoundError:
        print('FileNotFound')


words_file = 'words.txt'
text_file = 'input.txt'
output_file = 'output.txt'
# delete_file(words_file)
# delete_file(text_file)
# delete_file(output_file)

# create_file(words_file, 'quick is fault')
#
# create_file(
#     text_file,
#     """-I was quick to judge him, but it wasn't his fault.
# -Is this some kind of joke?! Is it?
# -Quick, hide here…It is safer.
# """
# )

try:
    target_words = get_text_as_list(words_file).split()
    target_text = get_text_as_list(text_file)

    create_file(output_file, '')
    result = {}
    for word in target_words:
        word_regex = fr'[\s\W]({word})[\s\W]'
        count = len(re.findall(word_regex, target_text, re.IGNORECASE))
        result[word] = count

    result = '\n'.join(f'{word} - {count}' for word, count in sorted(result.items(), key=lambda x: -x[1])) + '\n'

    write_to_file(output_file, result)
    print_file(output_file)
except AttributeError:
    print('AttributeError')
