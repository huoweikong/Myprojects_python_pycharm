#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/19 11:06
# software: PyCharm
import matplotlib.pyplot as plt

for idx, color in enumerate("rgb"):

    plt.subplot(320+idx+1, axisbg=color)
plt.show()

