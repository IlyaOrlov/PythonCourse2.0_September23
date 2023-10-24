import re


def find_git_commands(file_path):
    git_commands = []
    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(r'git\s+\w+', line)
            git_commands.extend(matches)

    return git_commands


file_path = 'Practice/README.md'
git_commands = find_git_commands(file_path)

for command in git_commands:
    print(command)
