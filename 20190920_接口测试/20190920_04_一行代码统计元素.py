#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-20 and 12:00
FileName:20190920_04_一行代码统计元素.py
Description：...
第四题
尽量用一行代码统计同时在两个列表中都出现的元素
如：l1=[1,2,3]
l2=[3,4,5]
重复出现的元素是3
'''
l1 = [1, 2, 3]
l2 = [3, 4, 5]
print("重复出现的元素：{}".format((i for i in l1 if i in l2).__next__()))

# --结果：重复出现的元素：3