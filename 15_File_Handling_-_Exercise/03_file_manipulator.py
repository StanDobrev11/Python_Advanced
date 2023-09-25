"""
Create a program that will receive commands until the command "End". The commands can be:
• "Create-{file_name}" - Creates the given file with empty content. If the file already exists, remove the
existing text in it (as if the file is created again)
• "Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist,
create it, and add the content
• "Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the
occurrences of the old string with the new string. If the file does not exist, print: "An error occurred"
• "Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"

Input               Comment
Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End
                    Create-file.txt The first command creates the empty file
                    After the first and second Add command, the
                    content is:
                    First Line
                    Second Line
                    On the first Replace command, an error must occur
                    After the next two Replace commands, the content
                    is:
                    1st Line
                    2nd Line
                    After the first Delete command, an error occurs
                    Finally, the 'file.txt' file is deleted
"""
# from os import truncate
import os


def get_filepath(filename):
    return f"txt_files/{filename}"


def create_file(args):
    filename = args[0]
    with open(get_filepath(filename), 'w'):
        print('File created/truncated')


def delete_file(args):
    filename = args[0]
    try:
        os.remove(get_filepath(filename))
        print('File deleted')
    except FileNotFoundError:
        print('An error occurred')


def add_content(args):
    filename, content = args
    try:
        with open(get_filepath(filename), 'a') as file:
            file.write(content + '\n')

    except FileNotFoundError:
        print('An error occurred')


def replace_content(args):  # Replace-test.txt-^-&
    filename, old_str, new_str = args
    try:
        with open(get_filepath(filename), 'r+') as file:
            text = file.read()
            text = text.replace(old_str, new_str)
            file.seek(0)
            # file.truncate()  # only if opened 'w+'
            file.write(text)

    except FileNotFoundError:
        print('An error occurred')


mapper = {
    'add': add_content,
    'replace': replace_content,
    'create': create_file,
    'delete': delete_file,
}
command = input().split('-')
while command[0] != "End":
    command, *rest_as_list = command
    mapper[command.lower()](rest_as_list)
    command = input().split('-')
