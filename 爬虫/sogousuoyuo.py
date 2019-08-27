#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/19 18:23
# software: PyCharm
import requests
url = "https://www.so.com/s"
keyword = "Python"
try:
    kv = {'q': keyword}
    r = requests.get(url, params=kv)
    print(r.request.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(len(r.text))
    print((r.text[:1000]))
except:
    print("爬取失败")