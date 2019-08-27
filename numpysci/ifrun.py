#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/10 13:21
# software: PyCharm
#条件运算

import numpy as np
#Numpy.where(condition, x, y)：三目运算满足condition，为x；不满足condition，则为y
score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 如果数值小于80，替换为0，如果大于等于80，替换为90
re_score = np.where(score < 80, 0, 100)
print(re_score)