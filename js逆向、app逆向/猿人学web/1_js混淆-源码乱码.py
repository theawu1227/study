import time
from js2py import require
import js2py
import requests
import execjs


def load_js():
    de = execjs.get()
    with open('demo1.js', 'r', encoding='utf-8') as r:
        cod = r.read()
    cods = de.compile(cod)
    return cods


def get_m():
    ti = int(time.time())
    # ti = 1667975673
    tim = ti * 1000 + (16798545 + -72936737 + 156138192)
    js = load_js()
    mm = js.call('m', str(tim))
    m = "丨".join([mm, str(int(tim / 1000))])
    return m


def parse(m):
    va = 0
    nus = 0
    for num in range(1, 6):
        ua = {
            "cookie": "sessionid=1mw7a8ppdc4kxyi2kcrowwcqwst33f0j",
            "user-agent": "yuanrenxue.project"
        }
        url = "https://match.yuanrenxue.com/api/match/1"
        param = {
            'page': num,
            'm': m
        }
        # print(param)
        response = requests.get(url, headers=ua, params=param).json()
        data = response['data']
        for da in data:
            va = va + da['value']
            nus+=1

    print(va/nus)


if __name__ == '__main__':
    # de = execjs.get()
    # nod = load_js()
    # ctx = de.compile(nod)
    # m = ctx.eval('get_sign()')
    m = get_m()
    parse(m)
    # print(m)
# print(int(time.time()))
