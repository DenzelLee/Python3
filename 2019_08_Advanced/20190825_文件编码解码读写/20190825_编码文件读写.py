#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-25 and 14:06
FileName:20190825_编码文件读写.py
Description：...
 文件：'utf8编码.txt', 'utf8编码的'
1. 将两个文件内容读出，合并内容到一个字符串中，并用print方法正确打印合并后的内容
2. 然后，程序用中文提示用户“请输入 新文件的名称”，用户输入文件名可以包含中文，将上面合并后的内容存储到一个新文件中，以utf8格式编码。
   新文件的文件名就是上面用户输入的名字。
'''
import time

# 定义本地文件夹的路径
filepath = "D:\MyTest\Python3\Tmp\\2019_08_Advanced\\"

# 定义当前年月日
nowTime = time.strftime('%Y-%m-%d',time.localtime(time.time()))

# 根据编码打开文件1和文件2
with open(filepath+"gbk编码.txt","r",encoding="gbk") as g,\
        open(filepath+"utf8编码.txt","r",encoding="utf8") as u:

    # 获取多个文件内容
    allread = f"--{g.read()}\n--{u.read()}"
    print(f"1.合并内容如下：\n{allread}\n")

    # 获取文件名称
    filename = str(input("请输入合并文件名>>>"))

    # 写入新文件（如果没有文件后缀.txt，默认文本文件）
    with open(filepath+f'{filename}{nowTime}.txt',mode="w+",encoding="utf8") as n:
        n.write(allread)

        # 光标重置到初始位置
        n.seek(0,0)
        # 新文件夹内容读取
        new = n.read()
        print(str(new))


# ----方法2：
# path = "D:\desktop\songqin\python进阶\day1\编码\python进阶测试-作业1-字符编码集-task07\cfiles"
#
# utf8Path = path + "\\utf8编码.txt"
# gbkPath = path + "\gbk编码.txt"
#
#
#
# newStr = ""
#
# with open(utf8Path, "r", encoding="utf8") as f:
#     newStr += f.read()
#
# newStr += "\n"
# with open(gbkPath, "r", encoding="gbk") as f:
#     newStr += f.read()
#
#
# print(newStr)
#
# file_name = input("请输入>>>")
#
#
# with open(path+"\\%s.txt" % file_name, "w", encoding="utf8") as f:
#     f.write(newStr)