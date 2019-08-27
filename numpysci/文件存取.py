#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/11 09:49
# software: PyCharm
import numpy as np
a = np.arange(0,12,1)
a.shape = 3,4

a.tofile("a.bin")


print(a.shape)
b = np.fromfile("a.bin", dtype=np.int64)
b.shape = 3,4
print(b)

np.save("a.npy", a)
c = np.load("a.npy")
print(c)

a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
np.savez("result.npz", a, b, sin_array = c)

r = np.load("result.npz")
print(r)
print(r["arr_0"])
print(r["arr_1"])      
print(r["sin_array"])