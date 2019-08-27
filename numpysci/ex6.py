#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/10 11:48
# software: PyCharm
import numpy as np

a = [1, 2, 3]
b = np.array(a)
c = np.array([[0, 1, 2, 10],
              [12, 13, 100, 101],
              [102, 110, 112, 113]], int)
print(c)
print(b)
array_one = np.ones([10, 10], dtype=np.int)
print(array_one)

array_zero = np.zeros([10, 9], dtype=np.float)
print(array_zero)
#创建指定数值的数组
print("创建指定数值的数组")
array_full = np.full((2, 3), 5)
print(array_full)

#创建单位矩阵
print("创建单位矩阵")
array_eye = np.eye(5)
print(array_eye)
#创建对角矩阵
print("创建对角矩阵")
array_diag = np.diag([10, 20, 30, 40],-1)
print(array_diag)
print(array_diag.size)
print(array_diag.shape)
print(array_diag.ndim)
print(array_diag.dtype)
print(array_diag.shape[1])
#Numpy创建随机数组（np.random）
array_rand = np.random.rand(10, 10, 4)
print(array_rand)
print(array_rand.ndim)
#创建指定范围内的一个数：Numpy.random.uniform(low, high, size=None)

array_uniform = np.random.uniform(0, 100, size=5)
print(array_uniform)

#创建指定范围的一个整数：Numpy.random.randint(low, high, size=None)
array_int = np.random.randint(0, 100, size=3)
print(array_int)
print(array_int.size)
#Numpy.arange()和Numpy.linspace()函数也可以均匀分布

#Numpy.arange(start, stop, step)：创建一个秩为1的array，其中包含位于半开区间[start, stop)内并均匀分布的值，step表示两个相邻值之间的差。
X = np.arange(1, 5, 2, dtype=np.int)
print(X)
#Numpy.linspace(start, stop, N)：创建N个在闭区间[start, stop]内均匀分布的值。
y = np.linspace(1, 5, 3)
print(y)
#正态分布
#创建给定均值、标准差、维度的正态分布：Numpy.random.normal(loc, scale, size)
# 正态生成4行5列的二位数组
array_normal = np.random.normal(loc=1.75, scale=0.1, size=[4, 5])
print(array_normal)
print(array_normal.ndim)
# 截取第0至第3行，第2至第4列（从第0行第0列算起）
after_array = array_normal[:3, 2:4]
print(after_array)
#数组的复制
#Numpy.copy(参数 1：数组)：创建给定array的一个副本，还可当做方法用。
after_array = array_normal[:3, 2:4].copy()
copy_array = np.copy(array_normal[:, 2:4])
print(after_array)
print(copy_array)
