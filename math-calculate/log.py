#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/7/5 16:08
# software: PyCharm
import math

#log a(di) B(zhen) = c(zhi)  a ** c = b
while True:
    a = input("请输入底数")
    b = input("请输入真数")
    c = input("请输入指数")

    if a == '':
        #利用pow(a, b)函数即可。需要开a的r次方则pow(a, 1.0/r)
        a = math.pow(float(b), 1/float(c))
    elif b == '':
        b = float(a) ** float(c)
    else:
        c = math.log(float(b), float(a))
    print("底数，真数，指数分别为：")
    print(a, b, c)
