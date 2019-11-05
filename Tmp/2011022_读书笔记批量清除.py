#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-10-22 and 16:53
FileName:2011022_读书笔记批量清除.py
Description：...
标题：读书笔记批量去除某一指定内容
'''
from selenium import webdriver
from pprint import pprint
from time import sleep
import datetime, time
from selenium.webdriver.support.ui import Select

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
count = 0
lines = [l for l in open(r"C:\Users\Administrator\Desktop\马云.txt", "r") if l.find(">> ", 0) != 0]
print(lines)
for i in lines:
    print(i)
fd = open(r"C:\Users\Administrator\Desktop\马云1.txt", "w")
fd.writelines(lines)
fd.close()