#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
Author:lihao
Date&Time:2019-06-14 and 22:09
FileName:手机号检测器
Description of parameters：Mobile移动, Unicom联通, Telecom电信

"""
import sys
# #sys.path.append(r"E:\我的课堂\Homework\20190710OS系统\第9次作业\模块与包-题目\第9次作业-模块与包-task06\task07\phone")
# sys.path.append(r"D:\MyTest\Python3\Tmp\2019_07_python\phone")
for i in sys.path:
    print(i)
print("...............相同目录下.............")
from apple import iphone6,iphone7
from samsung.note import galaxy_note8
from samsung.s import galaxy_s7
iphone6.askPrice()
iphone7.askPrice()
galaxy_note8.askPrice()
galaxy_s7.askPrice()
