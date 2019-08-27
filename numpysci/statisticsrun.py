#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/10 13:24
# software: PyCharm
import numpy as np
#统计运算
#指定轴最大值：amax(参数1：数组；参数2：axis=0/1，0表示行1表示列)
score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
print(score)
# 求整个矩阵的最大值
result = np.amax(score)
print(result)
# 求每一列的最大值（0表示行）
result = np.amax(score, axis=0)
print(result)
# 求每一行的最大值（1表示列）
result = np.amax(score, axis=1)
print(result)

# 指定轴最小值：amin(参数1：数组；参数2：axis=0/1，0表示行1表示列)
# 求整个矩阵的最小值
result = np.amin(score)
print(result)
# 求每一列的最小值（0表示行）
result = np.amin(score, axis=0)
print(result)
# 求每一行的最小值（1表示列）
result = np.amin(score, axis=1)
print(result)

# 指定轴平均值：mean(参数1：数组；参数2：axis=0/1，0表示行1表示列；参数3：dtype，输出数据类型)
# 求整个矩阵的平均值
result = np.mean(score, dtype=np.int)
print(result)
# 求每一列的平均值（0表示行）
result = np.mean(score, axis=0)
print(result)
# 求每一行的平均值（1表示列）
result = np.mean(score, axis=1)
print(result)
#指定轴方差：std(参数1：数组；参数2：axis=0/1，0表示行1表示列；参数3：dtype，输出数据类型)
# 求整个矩阵的方差
result = np.std(score)
print(result)
# 求每一列的方差（0表示列）
result = np.std(score, axis=0)
print(result)
# 求每一行的方差（1表示行）
result = np.std(score, axis=1)
print(result)