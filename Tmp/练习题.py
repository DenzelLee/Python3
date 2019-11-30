#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019/11/29 and 9:22
Project:Python3
FileName:练习题
Description：...
'''

for i in range(1, 10):
    for j in range(1, i+1):
        print(str(j)+" * "+str(i)+" = "+str(j*i), end="  ")
    print("")