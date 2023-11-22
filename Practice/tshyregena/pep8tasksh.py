import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler: # Название класса написано не правильно, как вариант написать с большой буквы

    def __init__(self): # Отсутствует параметр map
        self.map = {}

    def rename(self, dirname, output): # Может быть статическим методом
         mp3s = [] # Не выровнено, поэтому не видит
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname)) # Возможно ошибка в названии mp3
          f = open(output, 'r')
          f.write(str(self.map))

    def restore(self, dirname, restore_path): # Не принимает filename
          with open(filename, '+') as f: # проблема с выравниванием
            self.map = ast.literal_eval(f.read())
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        os.remove(restore_path)
                
     def generateName(self, seed=time()): # Название функции написано с ошибкой
          return hashlib.md5(str(seed)).hexdigest() # проблема с выравниванием


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
    Shuffler = shuffler() # ошибка в названии класса
    if args.subcommand == 'rename':
          if args.output:
                Shuffler.rename(args.dirname, 'restore.info')
          else:
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
