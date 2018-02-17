import sys
from PIL import Image


def main():
    if len(sys.argv) is 2:
        img = Image.open(sys.argv[1])
        (w, h) = img.size

        out = Image.new('RGB', (w, h))

        for y in range(h):
            for x in range(w):
                (r, g, b) = img.getpixel((x, y))
                lsb = r % 2
                if lsb is 0:
                    out.putpixel((x, y), (0, 0, 0))
                else:
                    out.putpixel((x, y), (255, 255, 255))

        out.save('lsb.png')


if __name__ == '__main__':
    main()
