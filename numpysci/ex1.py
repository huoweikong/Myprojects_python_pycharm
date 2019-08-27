#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 艾强云
# Email:1154282938@qq.com
# datetime:2019/4/5 01:43
# software: PyCharm
import numpy as np
x = np.arange(10, 1, -1)
print(x)
b = x[[3, 3, 1, 8]]
print(b)
b[2] = 100
print(b)
x = np.arange(5,0,-1)
print(x)
b = x[np.array([True, False, True, False, False])]
print(b)
