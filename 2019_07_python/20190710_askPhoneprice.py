#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:lihao
Date&Time:2019-07-10 and 22:38
FileName:
'''
'''
附件里压缩 了一个目录（见附件phone.zip），解压后结构如下。

phone
  ├─apple
  └─samsung
      ├─note
      └─s
这个目录里面对应了苹果、三星手机 的价格。
在相应目录里面，包含对应手机价格的python文件。
请同学们在维持目录结构不变的前提下，把这个目录结构做成名为python包。
然后，自己写一个Python程序调用 那个python包里面的每个
模块文件（共四个）里面的askPrice 函数，显示每种手机的价格
同学们先将那个phone包，和自己写的调用程序文件放在同一个目录下，
运行调用程序，显示各种手机价格
同学们再将那个phone包，和自己写的调用程序文件放在不同的目录下，
通过设置 sys.path 或者 环境变量PYTHONPATH，
来保证可以找到phone包，并成功调用。
'''
import sys
#sys.path.append(r"E:\我的课堂\Homework\20190710OS系统\第9次作业\模块与包-题目\第9次作业-模块与包-task06\task07\phone")
# sys.path.append(r"D:\MyTest\Python3\Tmp\2019_07_python\phone")
# sys.path.pop(-1)
for i in sys.path:
    print(i)
print("...............不同目录下.............")
from phone.apple import iphone6,iphone7
from phone.samsung.note import galaxy_note8
from phone.samsung.s import galaxy_s7
iphone6.askPrice()
iphone7.askPrice()
galaxy_note8.askPrice()
galaxy_s7.askPrice()



