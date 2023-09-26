import os


def save_extensions(dir_name):
    ext_list = {}
    for filename in os.listdir(dir_name):
        if os.path.isdir(f'{dir_name}/{filename}'):  # file = os.path.join(dir_name, filename)
            if 'DIR' not in ext_list:
                ext_list['DIR'] = []
            ext_list['DIR'].append(filename)
        else:
            ext = filename.split('.')[-1]
            if ext not in ext_list:
                ext_list[ext] = []
            ext_list[ext].append(filename)

    if 'DIR' in ext_list:
        for directory in ext_list['DIR']:
            get_data_as_str(save_extensions(f'{dir_name}/{directory}'))

    return ext_list


def get_data_as_str(ext_dct):
    data = '\n'
    for k, v in sorted(ext_dct.items(), key=lambda x: x[0]):
        data += f'{k}\n'
        for value in sorted(v):
            data += f'- - - {value}\n'

    with open('report.txt', 'a') as file:
        file.write(data)


current_dir = input()
content_list = {}
get_data_as_str(save_extensions(current_dir))
