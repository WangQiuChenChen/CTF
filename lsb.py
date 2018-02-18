import sys
from PIL import Image


def main():
    l = len(sys.argv)

    if l <= 1 or l >= 4:
        print('lsb.py <input file> <output file>')
        print('\t<input file> - input file name, e.g. secret.png')
        print('\t<output file> - output file name, e.g. a.png, default: lsb.png')
    else:
        img = Image.open(sys.argv[1])
        (w, h) = img.size

        out = Image.new('RGB', (w, h))

        for y in range(h):
            for x in range(w):
                (r, _, _) = img.getpixel((x, y))
                lsb = r % 2
                if lsb is 0:
                    out.putpixel((x, y), (0, 0, 0))
                else:
                    out.putpixel((x, y), (255, 255, 255))
        if l is 2:
            out.save('lsb.png')
        else:
            out.save(sys.argv[2])


if __name__ == '__main__':
    main()
