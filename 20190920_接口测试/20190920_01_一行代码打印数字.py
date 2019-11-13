#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-19 and 18:39
FileName:20190920_01_一行代码打印数字.py
Description：...
第一题
1.尽量用一行代码将字符串中出现的数字打印出来
str1='4a9eabc2-82ca-4986-86ef-2411ae3c0af8'
'''
import re
str1 = '4a9eabc2-82ca-4986-86ef-2411ae3c0af8'
print(''.join([i for i in str1 if re.findall(r"\d+", i)]))


# --结果：492824986862411308

a = 'sada,sadasd;dasd.dasd'
print([i for i in a if re.findall(r'[A-Za-z]',i)])
print(a.replace(";",",").replace(".",",").split(","))

