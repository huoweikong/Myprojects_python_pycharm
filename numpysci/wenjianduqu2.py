#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/11 10:59
# software: PyCharm
import numpy as np

a = np.arange(0,12,0.5).reshape(4,-1)

np.savetxt("a.txt", a) # 缺省按照'%.18e'格式保存数据，以空格分隔
b = np.loadtxt("a.txt")
print(b)
np.savetxt("a.txt", a, fmt="%d", delimiter=",") #改为保存为整数，以逗号分隔

c = np.loadtxt("a.txt",delimiter=",") # 读入的时候也需要指定逗号分隔
print(c)

a = np.arange(8)

b = np.add.accumulate(a)

c = a + b

f = open("result.npy", "wb")

np.save(f,a)
np.save(f, b)

np.save(f, c)

f.close()

f = open("result.npy", "rb")
print(np.load(f))
print(np.load(f))
print(np.load(f))

