#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/10 15:10
# software: PyCharm
#数组与数的运算（加、减、乘、除、取整、取模）
import numpy as np
score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
print(score)
# 循环数组行和列，每一个数值都加5
score[:, :] = score[:, :]+5
print(score)
# 循环数组行和列，每一个数值都减5
score[:, :] = score[:, :]-5
print(score)
# 循环数组行和列，每一个数值都乘以5
score[:, :] = score[:, :]*5
print(score)
# 循环数组行和列，每一个数值都除以5
score[:, :] = score[:, :]/5
print(score)
# 循环数组行和列，每一个数值除以5取整
score[:, :] = score[:, :] // 5
print(score)
# 循环数组行和列，每一个数值除以5取模
score[:, :] = score[:, :] % 5
print(score)

#数组间运算（加、减、乘、除），前提是两个数组的shape一样
#加：“+”或者np.add(a, b)　　减：“-”或者np.subtract(a, b)　　

#乘：“*”或者np.multiply(a, b)　　除：“/”或者np.divide(a, b)
c = score + score
d = score - score
e = score * score
# 分母数组保证每个数值不能为0
b = score / score
print("相加", c)
print("相减", d)
print("相乘", e)
print("相除", b)
'''Numpy.intersect1d(参数 1：数组a；参数 2：数组b)：查找两个数组中的相同元素

Numpy.setdiff1d(参数 1：数组a；参数 2：数组b)：查找在数组a中不在数组b中的元素

Numpy.union1d(参数 1：数组a；参数 2：数组b)：查找两个数组的并集元素

'''
