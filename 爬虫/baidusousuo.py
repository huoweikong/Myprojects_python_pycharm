#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/19 18:16
# software: PyCharm
import requests
url = "https://www.baidu.com/s"
keyword = "艾强云"
try:
    kv = {'wd': keyword}
    r = requests.get(url, params=kv)
    print(r.request.url)
    r.raise_for_status()
    #r.encoding = r.apparent_encoding
    print(len(r.text))
    print((r.text[:1000]))
except:
    print("爬取失败")