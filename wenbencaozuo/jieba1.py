#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/4/19 15:35
# software: PyCharm
import jieba
a = jieba.lcut("中国是一个伟大的国家")
print(a)
b = jieba._lcut_for_search("我们中国是一个伟大的国家")
print(b)