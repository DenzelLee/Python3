#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-27 and 18:09
FileName:20190827_案例_装饰器.py
Description：...
'''
import time
from random import randint
nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

# 流程一
print("----1.函数作用域----\n")
a = "第一层作用域"
def func1():
    b = "第二层作用域"
    print(2, a, b)
    def funcc1():
        c = "第三层作用域"
        print(3, a, b, c)
    return funcc1
A = func1()  # 相当于把funcc 传给A
A()

# 流程二
print("\n----2.函数作为参数传递----\n")
def foo2(func2):
    print("1.func：接收一个函数名作为参数，执行函数方法")
    func2()
def bar2():
    print("2.bar：定义一个函数作为参数传递，执行函数方法")
foo2(bar2)

# 流程三
print("\n----3.函数作为返回值返回----\n")
def foo3(func3):
    print("1.func：接收一个函数名作为参数，执行函数方法")
    return func3
def bar3():
    print("2.bar：定义一个函数作为参数传递，执行函数方法")
bar33 = foo3(bar3)
bar33()

# 流程四
print("\n----4.（函数闭包）延长了局部变量的生命周期----\n")
def info4(name):
    print("1.name:",name)
    def info4(age):
        print("2.'name:'", name, "'；age:'", age)
    return info4
name44 = info4("Alice")
name44(27)

# 简单装饰器
print("\n----5.简单装饰器----\n")
def show_time1(func):
    print("1.第一层函数：展示时间")
    def calc_time1():
        print("2.第二层函数：计算时间")
        start = time.time()
        func()
        end  = time.time()
        print("2-1完成时间：",start-end)
    return calc_time1
@show_time1
def func5(): # 其实就等于calc_time()
    print("3.重写第二层函数：计算时间")
    print("case1")
    time.sleep(1)
    print("case2")
# func5 = show_time1(func55)
func5()

# 带参数的装饰器1
print("\n----6.参数装饰器----\n")
def show_time6(func6):
    print("1.第一层函数：展示时间")
    def calc_time6(values):
        print("2.第二层函数：计算时间")
        start = time.time()
        func6(values)
        end  = time.time()
        print("2-1完成时间：",start-end)
    return calc_time6 # 装饰器重点在于返回值
@show_time6
def func6(value): # 其实就等于calc_time()
    print("3.重写第二层函数：计算时间")
    print("case1")
    time.sleep(value)
    print("case2")
# func6 = show_time(func6)
func6(1)

# 带参数的装饰器2
print("\n----7.参数装饰器----\n")
def add_show_time7(func6):
    print("1.第一层函数：展示时间")
    def calc_time7(*args):
        print("2.第二层函数：计算时间")
        start = time.time()
        func6(*args)
        end  = time.time()
        print("2-1完成时间：",start-end)
    return calc_time7 # 装饰器重点在于返回值
@add_show_time7
def add_func7(*args): # 其实就等于calc_time()
    count =0
    for i in args:
        count +=1
        print(count)
    time.sleep(1)
    return count
# func6 = show_time(func6)
add_func7(1,2,3,4)

# 带参数的装饰器3
print("\n----8.对象装饰器----\n")
def func8():
    print('1234')
func8()
print(type(func8))
func8 = '1234'
print(func8)
print(type(func8))