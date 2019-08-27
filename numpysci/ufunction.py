#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/11 00:41
# software: PyCharm
import numpy as np
from enthought.mayavi import mlab


a = np.arange(0,60,10).reshape(-1,1)
print(a)
print(a.shape)
b = np.arange(0,5)
print(b)
print(b.shape)
c = a + b
print(c)