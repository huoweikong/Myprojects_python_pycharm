#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/5 02:01
# software: PyCharm
import numpy as np
x = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
print(x)
print(x[0, 3:5])
print(x[:, 2])
print(x[4:, 4:])
print(x[2::2, ::2])
