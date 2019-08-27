#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/19 18:13
# software: PyCharm
import requests
#url = "https://item.jd.com/100004404934.html"
url = "https://www.amazon.cn/dp/B06XWQ9WY8/ref=cngwdyfloorv2_recs_0/459-6216834-4919212?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=D1ZWNWNYZMR23NC0V9M3&pf_rd_r=D1ZWNWNYZMR23NC0V9M3&pf_rd_t=36701&pf_rd_p=db4e96ef-5fc1-47f8-92b2-b9a5e737b326&pf_rd_p=db4e96ef-5fc1-47f8-92b2-b9a5e737b326&pf_rd_i=desktop"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)

    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print((r.text[1000:2000]))

except:

    print("爬取失败")
