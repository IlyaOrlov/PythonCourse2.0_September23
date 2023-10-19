import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Searches for pattern in image')
    parser.add_argument('-s', '--start', type=int, default=1, help='Аргумент старт')
    parser.add_argument('-f', '--stop', type=int, required=True, help='Аргумент стоп')
    parser.add_argument('-t', '--step', type=int, default=1, help='Аргумент шаг')
    return parser.parse_args()


def myrange(start, stop, step):
    while start < stop:
        yield start
        start += step


if __name__ == "__main__":
    args = parse_args()
    for i in myrange(args.start, args.stop, args.step):
        print(i)
