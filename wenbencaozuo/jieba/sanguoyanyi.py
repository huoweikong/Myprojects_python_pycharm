#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/19 15:57
# software: PyCharm
import jieba
txt = open("sanguoyanyi.txt",'r').read()
excludes = {"将军","却说","二人","一名","三人","天下","叔父","姓名","将军","大喜","颍川","封谞","太守"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

