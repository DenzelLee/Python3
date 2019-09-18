#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-18 and 15:08
FileName:pythonApi.py
Description：...
'''
from selenium import webdriver
from pprint import pprint
from time import sleep
import datetime, time

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
