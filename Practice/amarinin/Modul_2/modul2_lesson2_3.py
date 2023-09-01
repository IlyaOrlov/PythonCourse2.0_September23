import sys
import os
import hashlib
import ast
import argparse
from time import *  # такой импорт может привести к конфликту между именами в модуле 'time' и именами в коде


class shuffler:  # имя класса 'shuffler' не CamelCase

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []  # два лишних пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))  # в 'mp3)' лишняя скобка и 'hashname))' то же
          f = open(output, 'r')  # не хватает двух пробелов перед 'f'
          f.write(str(self.map))  # не хватает двух пробелов перед 'f'

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:  # два лишних пробела относительно 'def'
            self.map = ast.literal_eval(f.read())  # не хватает двух пробелов перед 'self.map'
          mp3s = []  # если относится к циклу 'with', то нет 4 пробела, иначе 2 лишних пробела относительно 'def'
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':  # не хватает пробела  перед 'if'
                    mp3s.append({root, file})  # один пробел лишний, относительно 'if'
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))  # лишняя скобка ')'
        os.remove(restore_path)  # если относится к циклу 'for', то не хватает 4 пробела
                
     def generateName(self, seed=time()):  # имя 'generateName' не snake_case и один лишний пробел
          return hashlib.md5(str(seed)).hexdigest()  # один лишний пробел


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args
# должна быть вторая пустая строка
def main():
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
          if args.output:  # два лишних пробела относительно 'if'
                Shuffler.rename(args.dirname, 'restore.info') #  два лишних пробела относительно 'if'
          else:  #  два лишних пробела относительно 'if'
                Shuffler.rename(args.dirname, args.output)  # два лишних пробела относительно 'else:'
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
