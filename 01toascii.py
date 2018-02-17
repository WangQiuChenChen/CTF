import re
import sys


def main():
    if len(sys.argv) is 2:
        s = re.findall(re.compile(r'.{7}'), sys.argv[1])
        dec = map(lambda x: int(x, 2), s)
        print(''.join(map(chr, dec)))


if __name__ == '__main__':
    main()
