#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-20 and 1:33
FileName:TestCase003_修改课程.py
Description：...
'''
from apiLibrary.apiTest import *
test = Course()
# 登录成功,获取cookies
test.login('auto', 'sdfsdfsdf')

# 列出课程数据
lcourse = test.list_course(1,20)
oldlist = lcourse['retlist']
print("当前课程数量："+str(len(lcourse['retlist'])))
print(str(lcourse['retlist'][1]['id']))

# 添加课程
checkC1 = f"测试课程{nowTime}"
checkC2 = f"测试描述{nowTime}"
addc = test.add_course(checkC1,checkC2,1)
assert addc['retcode'] ==0
cid = addc['id']

# 修改课程
mres = test.modify_course(cid,f'测试课程{nowTime}001',f'测试描述{nowTime}001',1)


# 列出课程数据
lcourse = test.list_course(1,20)
newlist = lcourse['retlist']
print("当前课程数量："+str(len(lcourse['retlist'])))

# 检查课程------------------------------------------------------------
print("\n----TestCase001（验证结果）----\n")

# 预期结果
checkCourse = {'id':cid,'name':f'测试课程{nowTime}001','desc':f'测试描述{nowTime}001','display_idx':1}

# 新列表-老列表=新课程
for course in newlist:
    if course not in oldlist:
        newCourse = course

# 验证响应码、新课程是否只出现1次、新课程是否等于预期结果
if mres['retcode'] == 0 and newlist.count(checkCourse) == 1 and newCourse == checkCourse:
    print("TestCase003 Pass:modify course success!\n")
    print(str(newCourse)+"\n"+str(checkCourse))

else:
    print("TestCase003 False:modify course fail!\n")
    print(str(newCourse)+"\n"+str(checkCourse))