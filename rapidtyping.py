import base64
import re

import requests


def main():
    url = 'http://121.42.176.204:23331/captcha/'
    r = requests.get(url)
    cookies = r.cookies
    html = r.text
    pattern = re.compile(r'<img src="data:image/svg.xml;base64,(.+)" />')
    b64 = re.findall(pattern, html)[0]
    svg = base64.decodestring(b64.encode('utf-8'))
    svgs = str(svg).split('</text>')
    svgs.pop()
    typing = ''
    for i in svgs:
        typing = typing + i[-1]
    r = requests.get(url, params={'code': typing}, cookies=cookies)
    print(r.text)


if __name__ == '__main__':
    main()
