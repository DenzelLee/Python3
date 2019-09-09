#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:lihao
Date&Time:2019-07-06 and 13:45
FileName:
'''
'''题目：现有文件1（如下，请保存到文件file1.txt中）， 记录了公司员工的薪资，其内容格式如下

name: Jack   ;    salary:  12000
 name :Mike ; salary:  12300
name: Luk ;   salary:  10030
  name :Tim ;  salary:   9000
name: John ;    salary:  12000
name: Lisa ;    salary:   11000

每个员工一行，记录了员工的姓名和薪资，
每行记录 原始文件中并不对齐，中间有或多或少的空格

现要求实现一个python程序，计算出所有员工的税后工资（薪资的90%）和扣税明细，
以如下格式存入新的文件 file2.txt中，如下所示

name: Jack   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Mike   ;    salary:  12300 ;  tax: 1230 ; income:  11070
name: Luk    ;    salary:  10030 ;  tax: 1003 ; income:   9027
name: Tim    ;    salary:   9000 ;  tax:  900 ; income:   8100
name: John   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Lisa   ;    salary:  11000 ;  tax: 1100 ; income:   9900

要求像上面一样的对齐
tax 表示扣税金额和 income表示实际收入。注意扣税金额和 实际收入要取整数  

'''
# inFile = r"E:\我的课堂\Homework\20190706小大排序\inFile.txt"
# outFile = r"E:\我的课堂\Homework\20190706小大排序\outFile.txt"
# with open(inFile, "r") as inFile1, open(outFile, "w") as outFile1:
#     for i in inFile1.read().splitlines():                         #全部读出来，然后用返回每一行到列表中
#         if i.count(";") == 1:
#             if i.count(":") < 1:
#                 continue
#             name = i.split(";")[0].split(":")[1].strip()
#             salary = int(i.split(";")[1].split(":")[1].strip())
#             tax = int(salary*0.1)
#             income = int(salary*0.9)
#             outInfo = "name:{:<10};salary:{:<10};tax:{:<10};income:{:<10}".format(name, salary, tax, income)
#             # print(outInfo)
#             outFile1.write(outInfo+"\n")
# outFile2=open(outFile1,"rb")


inFile = "E:\\我的课堂\\Homework\\20190706小大排序\\20190706员工工资.txt"
outFile = "E:\\我的课堂\\Homework\\20190706小大排序\\20190706员工工资2.txt"
inFile1 = open(inFile,'r')
outFile1 = open(outFile,'w')   #末尾追加内容
for info in inFile1.readlines():
    name = info.split(";")[0].split(":")[1].strip()
    salary = info.split(";")[1].split(":")[1].strip()
    tax = 0.1*int(salary)
    income = int(salary)-int(tax)
    outinfo = "name:{:<10};salary:{:<10};tax:{:<10};income:{:<10}".format(name, salary, tax, income)
    # print(outinfo)
    outFile1.write(outinfo+"\n")
outFile1.write("分割线~~~~~~~~~~~~~")
newFile=outFile1.read()
print(newFile)
inFile1.close()
outFile1.close()





