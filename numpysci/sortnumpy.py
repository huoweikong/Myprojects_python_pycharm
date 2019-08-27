#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/10 13:09
# software: PyCharm

import numpy as np
# 数组排序
# 键Numpy.sort(参数 1：a，数组；参数 2：axis=0/1，0表示行1表示列)：np.sort()作为函数使用时，不更改被排序的原始array；array.sort()作为方法使用时，会对原始array修改为排序后数组array
# 整体排序，每行或每列都会排序
array_normal = np.random.normal(loc=1.75, scale=0.1, size=[4, 5])
np.sort(array_normal)
# 仅行排序，上边小，下边大
a = np.sort(array_normal, axis=0)
# 仅列排序,最左边最小，右边大
b = np.sort(array_normal, axis=1)
print(array_normal)
print(a)
print(b)

# 数组唯一元素
# Numpy.unique(参数 1：a，数组；参数 2：return_index=True/False，新列表元素在旧列表中的位置；参数 3：return_inverse=True/False，旧列表元素在新列表中的位置；参数 4：return_counts，元素的数量；参数 5：axis=0/1，0表示行1表示列)：查找array中的唯一元素。
print("提取唯一元素", np.unique(array_normal))
print("提取唯一元素", np.unique(array_normal, return_index=True))
print("提取唯一元素", np.unique(array_normal, return_counts=True))
print("提取唯一元素", np.unique(array_normal, return_index=True, return_inverse=True, axis=0))

#reshape()：把指定的数组改变形状，但是元素个数不变；有返回值，即不对原始多维数组进行修改
c = np.array([[[0, 1, 2],
               [10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
"""
[[[  0   1]
  [  2  10]]

 [[ 12  13]
  [100 101]]

 [[102 110]
  [112 113]]]
"""
print(c.reshape(3, 2, 2))
"""
[[  0   1   2  10]
 [ 12  13 100 101]
 [102 110 112 113]]
"""
# 某一维指定为-1时，自动计算维度
print(c.reshape(3, -1))
"""[[[  0   1]
    [  2  10]
    [ 12  13]]

    [[100 101]
    [102 110]
    [112 113]]]"""
print(c.reshape(2, -1, 2))
#resize()：把指定的数组改变形状，但是元素个数可变，不足补0；无返回值，即对原始多维数组进行修改
a = np.array([[[0, 1, 2],
               [10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
b = np.array([[[0, 1, 2],
               [10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
'''[[0]
    [1]
    [2]]'''
a.resize((3, 1))
'''[[  0   1   2  10  12]
    [ 13 100 101 102 110]
    [112 113   0   0   0]]'''
b.resize((3, 5))
print(a)
print(b)
