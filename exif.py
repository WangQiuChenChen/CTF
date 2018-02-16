import exifread
import sys


def main():
    if len(sys.argv) is 2:
        f = open(sys.argv[1], 'rb')
        tags = exifread.process_file(f)
        f.close()
        for tag in tags:
            if isinstance(tags[tag], bytes):
                pass
            else:
                print(tag + ': ' + str(tags[tag]))


if __name__ == '__main__':
    main()
