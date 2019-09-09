#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-30 and 18:32
FileName:20190830_多线程读取网页内容.py
Description：...
先阅读下面关于Python requests 库的文章 ，了解 使用它去获取一个网页内容的方法。
http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
然后编写一个python程序，创建两个子线程，分别到下面的网址获取文本内容

http://mirrors.163.com/centos/6/isos/x86_64/README.txt
http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt

主线程等待这个两个子线程获取到信息后，将其内容依次合并后存入名为 readme89.TXT 的文件中
'''
import time,threading,requests

# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

text_str = ""
url1 = "http://mirrors.163.com/centos/6/isos/x86_64/README.txt"
url2 = "http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt"

# 创建锁对象
lock = threading.Lock()

# 定义线程函数
def addshread(num,url):
    global text_str
    print("\n----开始启动线程%s号----" %(num))

    # 获取网页内容
    re_text = requests.get(url=url).text

    # 涉及到重要数据操作，上锁
    lock.acquire()
    print("\n--%s号线程，已上锁" %(num))
    text_str = text_str + re_text +f"\n----{num}----\n"

    # 解锁
    lock.release()
    print("\n--%s号线程，已解锁" %(num))

if __name__ == '__main__':
    t1 = threading.Thread(target = addshread,args=("1",url1))
    t2 = threading.Thread(target = addshread,args=("2",url2))

    t1.start()
    t1.join()
    t2.start()
    t2.join()

    with open("./threadLock.txt","w") as w:
        w.write(text_str)
    with open("./threadLock.txt","r") as r:
        rtext = r.read()
        print(rtext)



# ---- 方法2：
# import requests, threading
# myStr = ""
# lock = threading.Lock() # 锁
#
# def foo(url):
#     global myStr
#     a = requests.get(url).text
#
#     lock.acquire() # 涉及到重要数据操作， 上锁
#     myStr += a
#     lock.release()
#
# t1 = threading.Thread(target=foo, args=("http://mirrors.163.com/centos/6/isos/x86_64/README.txt",))
# t2 = threading.Thread(target=foo, args=("http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt",))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# with open("./readme89.txt", "w", encoding="utf8") as f:
#     f.write(myStr)



# ---- 方法3：
# # coding=utf8
# import requests
# import threading
#
# urls = [
# 'http://mirrors.163.com/centos/build/rpmcompare5.pl.txt',
# 'http://mirrors.163.com/centos/6.9/isos/x86_64/README.txt',
# ]
# # 对应urls 依次存储网页文件内容, 先创建同样个数的元素占位
# fileContentList = [None for one in urls]
#
# # 锁对象，用来控制访问 fileContentList
# lock = threading.Lock()
#
# def thread_entry(idx,url):
#     print('thread #%s start' % idx)
#     r = requests.get(url)
#
#     # 注意上面的代码不应该放在获取锁的代码中
#     lock.acquire()
#     # 注意 r.text的类型是unicode，可以在文档中查到
#     fileContentList[idx] = r.text
#     lock.release()
#
#     print('thread #%s end' % idx)
#
# if __name__ == '__main__':
#     print('main thread start.')
#
#     threadpool = []
#
#     for idx,url in enumerate(urls):
#         t = threading.Thread(target=thread_entry,
#                           args=(idx,url))
#         t.start()
#         threadpool.append(t)
#
#     # 等所有 线程结束
#     for t in threadpool:
#         t.join()
#
#     # 所有线程结束后，所有内容都获取到了，合并内容
#     mergeTxt = '\n\n----------------------\n\n'.join(fileContentList)
#     print(mergeTxt)
#     with open('readme89.txt','w',encoding='utf8') as f:
#         f.write(mergeTxt)
#     print('main thread end.')



