#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-19 and 22:28
FileName:TestCase002_添加老课程.py
Description：...
'''

from apiLibrary.apiTest import *
test = Course()
# 登录成功,获取cookies
test.login('auto', 'sdfsdfsdf')

# 添加课程1
checkC1 = f"测试课程{nowTime}"
checkC2 = f"测试描述{nowTime}"
addc1 = test.add_course(checkC1,checkC2,1)

# 列出课程
listc = test.list_course(1,20)
oldlist = listc['retlist']
print(f"\n当前课程数量：{len(listc['retlist'])}")

# 添加重复课程1
addc2 = test.add_course(checkC1,checkC2,1)

# 列出课程
listc = test.list_course(1,20)
newlist = listc['retlist']
print(f"当前课程数量：{len(listc['retlist'])}")


# 检查课程------------------------------------------------------------
print("\n----TestCase001（验证结果）！！！！----\n")

# 检查点，预期结果
checkCourse = {
    'id':addc1['id'],
    'name':f'{checkC1}',
    'desc': f'{checkC2}',
    'display_idx': 1
}

# 验证响应码、新课程是否只出现1次、新课程是否等于预期结果
if addc2['retcode'] == 2 and newlist.count(checkCourse) == 1:
    print("TestCase002 Pass:add course fail!\n")
    print(oldlist,"\n",newlist)
    print("\n"+str(addc2))

else:
    print("TestCase002 Pass:add course success!\n")
    print(oldlist,"\n",newlist)
    print("\n"+str(addc2))