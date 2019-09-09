#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-27 and 17:55
FileName:Oracle_database.py
Description：...
'''
# pip install cx_Oracle
import time
import cx_Oracle as oracle

nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
db = oracle.connect('icbc_isv/CxTjTWf1Tono8EQVQJJhu@//172.16.78.84:1521/ICBC_ISV')
cursor = db.cursor()
cursor.execute('select user from dual')
for line in cursor.fetchall():
    print(line)
