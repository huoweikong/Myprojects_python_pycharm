#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/19 18:07
# software: PyCharm
import requests
url = "https://www.amazon.cn/Kindle%E5%95%86%E5%BA%97/b/ref=sa_menu_top_kindle_l1_store?ie=UTF8&node=116087071"
kv = {'user-agent': 'Mozilla/5.0'}
r = requests.get(url, headers=kv)
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
r.encoding = r.apparent_encoding

print(r.text[:1000])