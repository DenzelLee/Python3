#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-18 and 15:26
FileName:TestCase001_添加新课程.py
Description：...
'''
from apiLibrary.apiTest import *
test = Course()
# 登录成功,获取cookies
test.login('auto', 'sdfsdfsdf')

# 列出课程
listc = test.list_course(1,20)
oldlist = listc['retlist']
print(f"\n当前课程数量：{len(listc['retlist'])}")

# 添加课程
checkC1 = f"python名称{nowTime}"
checkC2 = f"python描述{nowTime}"
addc = test.add_course(checkC1,checkC2,1)


# 列出课程
listc = test.list_course(1,20)
newlist = listc['retlist']
print(f"当前课程数量：{len(listc['retlist'])}")

# 检查课程------------------------------------------------------------
print("\n----TestCase001（验证结果）----\n")

# 新列表-老列表=新课程
for course in newlist:
    if course not in oldlist:
        newCourse = course

# 检查点，预期结果
checkCourse = {
    'id':addc['id'],
    'name':f'{checkC1}',
    'desc': f'{checkC2}',
    'display_idx': 1
}

# 验证响应码、新课程是否只出现1次、新课程是否等于预期结果
if addc['retcode'] == 0 and newlist.count(checkCourse) == 1 and newCourse == checkCourse:
    print("TestCase001 Pass:add course success!\n")
    print(str(newCourse)+"\n"+str(checkCourse))

else:
    print("TestCase001 False:add course fail!\n")
    print(str(newCourse)+"\n"+str(checkCourse))


# # 清除数据
# for one in newlist:
#     if one['id'] == addc['id']:
#         test.delete_course(one['id'])

# # 列出清除后的课程数据
# lcourse = test.list_course(1,20)
# print("当前课程数量："+str(len(lcourse['retlist'])))



