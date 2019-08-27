#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/7/8 23:05
# software: PyCharm
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[6], [8], [10], [14], [18]]).reshape(-1, 1)

y = [7, 9, 13, 17.5, 18]

plt.figure()
plt.title('Pizza price plotted against diameter')
plt.xlabel("diameter in inches")
plt.ylabel('Price in dollars')
plt.plot(X, y, 'k.')
plt.axis([0, 25, 0, 25])
plt.grid(True)


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)

test_pizza = np.array([[12]])
predicted_price = model.predict(test_pizza)[0]
print('A 12" pizza should cost: $%.2f' % predicted_price )
plt.show()