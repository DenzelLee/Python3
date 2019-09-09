#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-01 and 20:29
FileName:hello.py
Description：...
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
print(f"{nowTime}.hello_world!")