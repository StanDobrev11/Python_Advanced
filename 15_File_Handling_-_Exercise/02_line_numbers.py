"""
Write a program that reads a text file, inserts line numbers in front of each line, and counts all the letters and
punctuation marks. The result should be written in another text file.

text.txt                            output.txt
-I was quick to judge him, but it
wasn't his fault.
-Is this some kind of joke?! Is
it?
-Quick, hide here. It is safer.
                                    Line 1: -I was quick to judge him, but it
                                    wasn't his fault. (37)(4)
                                    Line 2: -Is this some kind of joke?! Is it?
                                    (24)(4)
                                    Line 3: -Quick, hide here. It is safer.
                                    (22)(4)
"""
import re
from string import punctuation

file_ = 'txt_files/02_text.txt'

with open(file_) as file:
    line_count = 1

    for line in file:
        letters, symbols = 0, 0
        for symbol in line:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                symbols += 1

        with open('txt_files/02_output.txt', 'a') as file_out:
            file_out.write(f"Line {line_count}: {line.strip()} ({letters})({symbols})\n")

        line_count += 1

with open('txt_files/02_output.txt') as file_out:
    print(file_out.read())
