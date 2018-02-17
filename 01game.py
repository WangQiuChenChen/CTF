import sys
from math import sqrt

from PIL import Image


def main():
    if len(sys.argv) is 2:
        f = open(sys.argv[1], 'r')
        s = f.read()
        f.close()
        w = h = int(sqrt(len(s)))
        img = Image.new('RGB', (w, h))
        for i in range(len(s)):
            x = int(i % w)
            y = int(i / w)
            if s[i] is '0':
                img.putpixel((x, y), (0, 0, 0))
            else:
                img.putpixel((x, y), (255, 255, 255))
        img.save('01game.png')


if __name__ == '__main__':
    main()
