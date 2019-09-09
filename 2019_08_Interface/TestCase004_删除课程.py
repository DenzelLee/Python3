#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-21 and 12:48
FileName:TestCase004_删除课程.py
Description：...
'''
from apiLibrary.apiTest import *
test = Course()
# 登录成功,获取cookies
test.login('auto', 'sdfsdfsdf')

# 列出课程数据
lcourse = test.list_course(1,20)
print("当前课程数量："+str(len(lcourse['retlist'])))

# 获取课程id列表
idList = []
for id in lcourse['retlist']:
    idList.append(id['id'])

# 批量删除课程数据
try:
    for i in idList[0:]:
        delres = test.delete_course(i)
        if delres['retcode'] !=0:
            print(delres)
except Exception as e:
    print(e)


# 列出删除后的课程数据
lcourse = test.list_course(1,20)
print("当前课程数量："+str(len(lcourse['retlist'])))

if lcourse['total'] == 0:
    print("TestCase004 Pass:delete course success!\n")
else:
    print("TestCase004 Fail:delete course fail!\n")