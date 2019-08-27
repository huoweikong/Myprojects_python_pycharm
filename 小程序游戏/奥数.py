#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:艾强云 
# Email:1154282938@qq.com
# datetime:2019/8/20 10:15
# software: PyCharm
import itertools

for i in itertools.permutations(map(str, range(10)), 4):
    if int('{0}{1}{0}'.format(i[2], i[3])) + int(''.join(i[:3])) == int(''.join(i)):
        print('YAO:{}, ZUO:{}, HAO:{}, SHI:{}'.format(*i))



