#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-18 and 17:58
FileName:config.py
Description：...
'''
from selenium import webdriver
from pprint import pprint
from time import sleep
import datetime, time

inurl =r"http://localhost:8066/mgr/login/login.html"
outrul = r"http://localhost:8066/mgr/login/login.html"
database = ['localhost', '8066']
userinfo = {"user": "auto", "password": "sdfsdfsdf"}
