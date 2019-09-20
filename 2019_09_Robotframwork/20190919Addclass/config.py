#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-18 and 17:58
FileName:langconv.py
Description：...
'''
from selenium import webdriver
from pprint import pprint
from time import sleep
import datetime, time

# 内部环境配置
insideDatabase = ['localhost', '8066']
insideUrl =f'http://{insideDatabase[0]}:{insideDatabase[1]}/mgr/login/login.html'
insideUserinfo = {"username": "auto", "password": "sdfsdfsdf"}


# 外部环境配置
externalDatabase = ['localhost', '8066']
externalUrl =f'http://{insideDatabase[0]}:{insideDatabase[1]}/mgr/login/login.html'
externalUserinfo = {"username": "auto", "password": "sdfsdfsdf"}