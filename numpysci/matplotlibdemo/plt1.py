#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/19 10:54
# software: PyCharm
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$",color="green",linewidth=1.5)
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()