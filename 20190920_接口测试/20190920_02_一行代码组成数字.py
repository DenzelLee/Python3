#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-20 and 10:18
FileName:20190920_02_一行代码组成数字.py
Description：...
第二题
2.尽量用一行代码将字符串'127.0.0.1'中出现的点清除掉，
并重新组成一个没有点的字符串'127001'
'''
import re
local = "127.0.0.1"
print(re.sub(r"\.+", "", local))

# --结果：127001

