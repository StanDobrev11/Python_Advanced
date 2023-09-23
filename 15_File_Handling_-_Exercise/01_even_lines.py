"""
Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0. Before you
print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

text.txt                                output
-I was quick to judge him, but it
wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer.
                                        fault@ his wasn't it but him@ judge to
                                        quick was @I
                                        safer@ is It here@ hide @Quick@
"""

import os.path
import re

file_ = 'txt_files/01_text.txt'

regex = r'[-\?\!\,\.]'
count = 0
with open(file_) as file:
    for line in file:
        if count % 2 == 0:
            re_line = re.sub(regex, '@', line).strip('\n').split()
            re_line.reverse()
            print(' '.join(re_line))
        count += 1
