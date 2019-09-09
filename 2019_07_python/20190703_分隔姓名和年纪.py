#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:lihao
Date&Time:2019-07-04 and 20:24
FileName:
'''
# 学生信息：Jack Green ,   21  ;  Mike Mos, 9;
# 规则一：学生信息之间用分号隔开（分号前后可能有不定数量的空格）
# 规则二：每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格）
# Jack Green :   21;
# Mike Mos   :   09;
# 结果如上：学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零
# ----------------------------------
getName = input("请输入您的姓名和年龄，并以分号结束：")
getName1 = getName.split(";")
# print(getName1)
for i in getName1:
    # print(i)
    if ',' in i:
        name,age = i.split(",")
        name = str(name).strip()
        age = str(age).strip()
        print('%-20s:%02d' % (name,int(age)))
        print('{:<20}:{:0>2}'.format(name,age))
        print(f'{name:<20}:{age:0>2}')
