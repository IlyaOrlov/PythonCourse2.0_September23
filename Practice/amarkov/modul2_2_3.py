import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler: # название классов с большой буквы.

    def __init__(self):
        self.map = {} # в конце инструкции ставится двоеточие ?
# отступ между строк в 1 строку должен быть (?) т.к. это не крупные блоки
    def rename(self, dirname, output):
        mp3s = [] # конец инструкции двоеточие должно быть?

    for root, directories, files in os.walk(dirname): # должна быть ";" между инструкциями, на одной строке они не должны все располагаться
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append([root, file])
    for path, mp3 in mp3s:
        hashname = self.generateName() + '.mp3'
        self.map[hashname] = mp3
        os.rename(path + '/' + mp3), path + '/' + hashname))
        f = open(output, 'r')
        f.write(str(self.map))

    def restore(self, dirname, restore_path):
        with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read())
        mp3s = []

    for root, directories, files in os.walk(dirname):
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append({root, file})
    for path, hashname in mp3s:
        os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        os.remove(restore_path)

    def generateName(self, seed=time()):
        return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser() #не хватает двоеточия в конце
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help') #не хватает ;
    rename_parser = subparsers.add_parser('rename', help='rename help') # нет ;
    rename_parser.add_argument('dirname') # отсутствует двоеточие
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored') # длинную строку нужно разбить, в конце нет :
    restore_parser = subparsers.add_parser('restore', help="command_a help") # отсутствует : в конце строки
    restore_parser.add_argument('dirname') #нет двоеточия в конце строки
    restore_parser.add_argument('restore_map') #нет двоеточия в конце строки
    args = parser.parse_args() #нет двоеточия в конце строки
    return args


def main():
    args = parse_arguments()
    Shuffler = shuffler()
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