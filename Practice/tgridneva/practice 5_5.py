def replace_tabs(file_path, use_tabs):
    with open(file_path, 'r+') as file:
        content = file.read()

        if use_tabs:
            content = content.replace(' ' * 4, '\t')
        else:
            content = content.replace('\t', ' ' * 4)
        file.seek(0)
        file.write(content)
        file.truncate()


file_path = 'file.txt'
use_tabs = True

replace_tabs(file_path, use_tabs)
