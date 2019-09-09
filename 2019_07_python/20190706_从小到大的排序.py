#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:lihao
Date&Time:2019-07-06 and 10:35
FileName:
'''
'''
题目：请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。

请按下面算法的思路实现函数：

1. 创建一个新的列表newList
2. 先找出所有元素中最小的，append在newList里面
3. 再找出剩余的所有元素中最小的，append在newList里面
4. 依次类推，直到所有的元素都放到newList里面 
'''
oldList1 = [9,1,8,2,7,3,4,6,5,5]           #公共参数
oldList1 = [1,3,5,7,34,23,55,56,2,3,4,4,1] #公共参数
#列表从小到达排序，返回新列表
def mySort3(oldList):
    newList = []
    # 条件1：判断是否为列表
    if type(oldList) == list:
        # 条件2：判断是否为全整数（整数列表不能直接转换成str，需要把每个元素变成str，然后"".jion成str）
        if str("".join([str(x) for x in oldList])).isdigit() == True:
            for i in range(0,len(oldList)):
                for j in range(0,len(oldList)-1):
                    if oldList[j] > oldList[j+1]:
                        oldList[j],oldList[j+1] = oldList[j+1],oldList[j]
                # print(oldList)
                newList.append(oldList.pop(-1))
        else:
            print("mySort函数，参数的子元素类型错误，必须为Number")
    else:
        print("mySort函数，参数类型错误，必须为List")
    return newList
print(mySort3(oldList1))

# def mySort4(oldList):
#     newList = []
#     newList1 = []
#     while len(oldList1) != 0:
#         mixNum = oldList1[0]  # 默认最小值
#         mixDex = 0  # 默认最小值下标
#         dex = 0  # 动态下标
#         for i in oldList:
#             if mixNum > i:
#                 mixNum = i  # 以小换大，交换位置
#                 mixDex = dex  # 记录交换位置元素的下标
#             dex += 1  # 不管是否交换位置，都加1
#
#         newList.append(mixNum)  # 直接添加最小值
#         newList1.append(oldList.pop(mixDex))  # 末尾删除法添加
#
#     return newList, newList1
#
#
# print(mySort4(oldList1))




# 课堂笔记
# def mySort1(oldList):#列表从小到大排序
#     for i in range(0,len(oldList)-1):
#         for j in range(0,len(oldList)-1-i):
#             if oldList[j] > oldList[j+1]:
#                 oldList[j],oldList[j+1] = oldList[j+1],oldList[j]
#     print(oldList)
#
# def mySort2(oldList):#列表从大到小排序
#     for i in range(0,len(oldList)-1):
#         for j in  range(0,len(oldList)-1-i):
#             if oldList[j] < oldList[j+1]:
#                 oldList[j],oldList[j+1] = oldList[j+1],oldList[j]
#     print(oldList)
#
# mySort1(oldList1)
# mySort2(oldList1)