#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-20 and 12:25
FileName:20190920_06_打印和输出类方法.py
Description：...
第六题
定义一个python类IOString，有两个成员方法get_String 和 print_String
get_String 获取用户输入
print_String 将获取的输入信息大写输出
请写出类的实现，并分别调用这两个方法
'''
class IOString():
    # 获取用户输入信息
    def get_String(self):
        self.gettext = input("\n请输入您的信息：")

    # 打印用户输入信息
    def print_String(self):
        print(f"请确认您的输入：{self.gettext.upper()}")

if __name__ =="__main__":
    info = IOString()
    info.get_String()
    info.print_String()

# --结果：
# 请输入您的信息：hello world
# 请确认您的输入：HELLO WORLD