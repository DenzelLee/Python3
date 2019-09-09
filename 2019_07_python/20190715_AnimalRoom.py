#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:lihao
Date&Time:2019-07-15 and 12:47
FileName:
'''
'''
要求大家用面向对象的设计编写一个python程序，实现一个文字游戏系统。
动物园里面有10个房间，房间号从1 到 10。
每个房间里面可能是体重200斤的老虎或者体重100斤的羊。
游戏开始后，系统随机在10个房间中放入老虎或者羊。
然后随机给出房间号，要求游戏者选择敲门还是喂食。
如果选择喂食：
喂老虎应该输入单词 meat，喂羊应该输入单词 grass
喂对了，体重加10斤。 喂错了，体重减少10斤
如果选择敲门：
敲房间的门，里面的动物会叫，老虎叫会显示 ‘Wow !!’,羊叫会显示 ‘mie~~’。 动物每叫一次体重减5斤。
游戏者强记每个房间的动物是什么，以便不需要敲门就可以喂正确的食物。
游戏3分钟结束后，显示每个房间的动物和它们的体重。
实现过程中，有什么问题，请通过课堂上讲解的调试方法，尽量自己发现错误原因。
'''

from random import randint
import time
class Tiger(object):
    className = 'Tiger'
    def __init__(self, inWeight=200):
        # print("Tiger 实例属性体重为：", inWeight)
        self.weight = inWeight
    def roar(self):
        print("老虎大叫一声：wow！")
        self.weight -= 5
    def eat(self, inFood):
        if inFood == 'meat':
            print("老虎吃肉！+10")
            self.weight += 10
        else:
            print("老虎吃垃圾食品!-10")
            self.weight -= 10
class Sheep(object):
    className = 'Sheep'

    def __init__(self, inWeight=100):
        # print("Sheep 实例属性体重为：", inWeight)
        self.weight = inWeight

    def roar(self):
        print("Sheep大叫一声：mie！")
        self.weight -= 5

    def eat(self, inFood):
        if inFood == 'grass':
            print("Sheep吃草！")
            self.weight += 10
        else:
            print("Sheep吃垃圾食品!")
            self.weight -= 10
class Room:
    # className = 'Room'
    def __init__(self, inNumber, inAnimal):
        self.num = inNumber
        self.animal = inAnimal
        # print("Room 实例属性房间号和动物名为：", self.num, self.animal)
roomList = []
count = 0
for r in range(1, 11):
    if int(randint(0,1))==0:
        # print( "房间里面是老虎")
        ani = Tiger(200)
    else:
        # print( "房间里面是绵羊")
        ani = Sheep(100)
    room = Room(r,ani)
    roomList.append(room)
    count += 1
    # print(count)
# print("随机房间为：", roomList)
curTime = time.time()
while True:
    endTime = time.time()
    if (endTime-curTime) >10:
        for i,room in enumerate(roomList):
            print("游戏结束：{},{},{}".format(i+1,room.animal.className,room.animal.weight))
        break
    num = randint(1,10)
    room = roomList[num-1]
    cmd =input("Welcome to my room {},please input your cmd Y/N".format(room.num))
    if cmd == 'y':
        room.animal.roar()
    food = input("input your food:")
    room.animal.eat(food)

# import time
# from random import randint
#
# class Tiger:
#     className = 'Tiger'
#     def __init__(self,inWeight):
#         self.weight = inWeight
#         print("老虎体重：", self.weight)
#     def tell(self):
#         print("老虎吼叫：WOW!")
#         self.weight -=5
#     def eat(self,inFood):
#         self.food = inFood
#         if inFood == "meat":
#             self.weight += 10
#             print("老虎吃肉！+10斤")
#         else:
#             self.weight -= 10
#             print("老虎吃菜！-10斤")
# class Sheep:
#     className = 'Tiger'
#     def __init__(self,inWeight):
#         self.weight = inWeight
#         print("绵羊体重：", self.weight)
#     def tell(self):
#         print("绵羊吼叫：mie!")
#         self.weight -=5
#     def eat(self,inFood):
#         self.food = inFood
#         if inFood == "grass":
#             self.weight += 10
#             print("绵羊吃菜！+10斤")
#         else:
#             self.weight -= 10
#             print("绵羊吃肉！-10斤")
# class Room:
#     className = 'Room'
#
#     def __init__(self, inNumber, inAnimal):
#         self.num = inNumber
#         self.animal = inAnimal
# aList = []
# for i in range(1, 11):
#     if randint(1, 2) == 1:
#         animal1 = Tiger(200)
#     else:
#         animal1 = Sheep(100)
#     newRoom = Room(i, animal1)
#     aList.append(newRoom)
# curTime = time.time()
# while True:
#     endTime = time.time()
#     if (endTime - curTime) > 15:
#         for one in aList:
#             print("房间号：{}，动物名称：{}，动物体重：{}".format(one.num, one.animal.className, one.animal.weight))
#         break
#     numroom = randint(1,10)
#     room1 = aList[numroom-1]
#     cmd = input("welcome to {} room,please input your cmd Y/N?  :".format(numroom))
#     if cmd == 'Y' or cmd == 'y':
#         room1.animal.tell()
#     food = input("please input your food: ")
#     room1.animal.eat(food)









