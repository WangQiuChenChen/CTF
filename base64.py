import base64
from sys import argv


def main():
    if len(argv) is 2:
        encode = base64.encodebytes(argv[1].encode('utf-8'))
        print('Encode: ', end='')
        print(encode.decode('utf-8'))
        decode = base64.decodebytes(argv[1].encode('utf-8'))
        print('Decode: ', end='')
        print(decode.decode('utf-8'))


if __name__ == '__main__':
    main()
