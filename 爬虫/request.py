#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/19 16:56
# software: PyCharm
import requests
r = requests.get("http://www.baidu.com")
rs = r.status_code
print(rs)
print(r.headers)
print(r.text)
print(r.encoding)
print(r.apparent_encoding)
print(r.content)
r.encoding = "utf-8"
print(r.text)