#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:17:40 2019

@author: aiqiangyun
"""


import re
p = re.compile(r'［.*?］')
f = open('括号替换—分子生物学综述.txt','r')
str = f.read()
f.close()
str2=p.sub('', str)
with open('替换后.txt','w') as f:
    f.write(str2)