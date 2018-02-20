import re

import requests


def main():
    URL = 'http://121.42.176.204:23331/calculator/'
    r = requests.get(URL)
    c = r.cookies
    print(c)
    html = r.text
    # print(html)
    pattern = re.compile(r'<span id="exp">(.+) = </span>')
    ev = re.findall(pattern, html)[0]
    ans = eval(ev)
    print(ans)
    r = requests.get(URL, params={'answer': ans}, cookies=c)
    print(r.text)

if __name__ == '__main__':
    main()
