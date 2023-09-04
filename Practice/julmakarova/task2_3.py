import sys
import os
import hashlib
import ast
import argparse
from time import *


# Имя класса должно быть в CamelCase
class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        # Очередной уровень вложенности должен быть через 4 пробела (в данном случае 6)
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            # Неразбериха со скобочками в параметрах метода rename
            os.rename(path + '/' + mp3), path + '/' + hashname))
        # Ошибка в уровне вложенности из-за количества пробелов
          f = open(output, 'r')
          f.write(str(self.map))

    def restore(self, dirname, restore_path):
        # Очередной уровень вложенности должен быть через 4 пробела (в данном случае 6)
          with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                # Очередной уровень вложенности должен быть через 4 пробела (в данном случае 3)
               if file[-3:] == '.mp3':
                   # Очередной уровень вложенности должен быть через 4 пробела (в данном случае 5)
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            # Неразбериха со скобочками в параметрах метода rename
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        os.remove(restore_path)

    # Метод класса объявлен с уровнем вложенности 5 пробелов вместо требуемых 4
     def generateName(self, seed=time()):
         # Очередной уровень вложенности должен быть через 4 пробела (в данном случае 5)
          return hashlib.md5(str(seed)).hexdigest()


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

def main():
    args = parse_arguments()
    # Имя переменной должно быть в snake_case
    Shuffler = shuffler()
    if args.subcommand == 'rename':
        # Очередной уровень вложенности должен быть через 4 пробела (в данном случае 6)
          if args.output:
              # Очередной уровень вложенности должен быть через 4 пробела (в данном случае 6)
                Shuffler.rename(args.dirname, 'restore.info')
          else:
              # Очередной уровень вложенности должен быть через 4 пробела (в данном случае 6)
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
