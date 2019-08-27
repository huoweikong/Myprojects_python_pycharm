#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/19 17:13
# software: PyCharm
import requests
print("dsfsfsd")
try:
    r = requests.get("http://www.baidu.com", timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

except:
    return "产生异常"