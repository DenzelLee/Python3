#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-02 and 10:06
FileName:20190827_案例_多线程并发并行.py
Description：...
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

#----1.线程的创建和调用
'''
import threading
def say(num):
    print("running on number:%s" % num)
    time.sleep(3)
if __name__=='__main__':
    # 启动2个线程实例
    t1 = threading.Thread(target=say,args=(1,))
    t2 = threading.Thread(target=say,args=(2,))
    # 启动线程
    t1.start()
    t2.start()
    # 获取线程名称
    print(f'{t1.getName()}')
    print(f'{t2.getName()}')
    print("--线程结束")
'''

#----2.join子线程未结束，主线程将一直等待其结束，才结束
'''
import threading
def music():
    print("1.听音乐")
    time.sleep(1)
def movies():
    print("2.看电影")
    time.sleep(3)
# 生成2个线程实例
t1 = threading.Thread(target=music)
t2 = threading.Thread(target=movies)
# 启动线程
t1.start()
t2.start()
t1.join()
t2.join()
print("3.主线程结束！")
'''

#----3.串行和并行的任务节省时间差
'''
print("----串行运行----")
import time
starttime3 = datetime.datetime.now().second

def cthread(info,sec):
    time.sleep(sec)
    print(info)
# CPU处理需要1秒，磁盘写入需要3秒
cthread("CPU开始处理任务", 1)
cthread("磁盘开始处理任务", 1)
# 主线程执行时间
endtime3 = datetime.datetime.now().second
print("主线程完成时间>>>", endtime3-starttime3)

print("\n----并行运行----")
import threading
starttime = time.time()
def bthread(num):
    time.sleep(1)
    print(f"{num}子线程运行结束")

# 生成2个线程实例
t1 = threading.Thread(target=bthread,args=(1,))
t2 = threading.Thread(target=bthread,args=(2,))

# 启动线程
t1.start();t2.start();t1.join();t2.join()
endtime = time.time()
# 如果串行任务有等待时间（简称阻塞密集型任务），并行将会节约一般的时间，
# 但是如果是单纯的不中断的计算密集型任务场景，两者执行时间几乎没有差距
print("主线程完成时间>>>",endtime-starttime)
'''
#----4.不安全的银行卡多线程任务(不加锁金额会乱）
'''
import threading
account_balance = 500 # 当前银行卡余额500元
l = threading.Lock() # ---创建一把锁对象,记得要加括号

def money(num):
    l.acquire() # ---锁住进程,解锁才可以使用新进程
    global account_balance # 调用外部全局变量
    balance = account_balance # 获取余额
    balance += num
    time.sleep(1)
    account_balance = balance
    print("当前余额>>>",account_balance)
    l.release() # ---释放资源：解锁
t1 = threading.Thread(target=money,args=(-300,))
t2 = threading.Thread(target=money,args=(10000,))

t1.start()
t2.start()
t1.join()
t2.join()
print("---进程结束，正确余额：10200")
'''

#----5.双方僵持的死锁（递归锁或可重入锁）,表示支持多层上锁，直到全部释放，才能开启新线程
'''
print("----死锁----")
import time,threading
la = threading.Lock() #记得要加括号
lb = threading.Lock()

def add1():
    la.acquire()
    print("--la已上锁")
    time.sleep(1)
    lb.acquire()
    print("--lb已上锁")
    # la和lb都上锁后，la和lb都没法使用资源，就会形成死锁
    lb.release()
    print("--lb已解锁")
    la.release()
    print("--la已解锁")


def add2():
    lb.acquire()
    print("--lb已上锁")
    time.sleep(3)
    la.acquire()
    print("--la已上锁")
    lb.release()
    print("--lb已解锁")
    la.release()
    print("--la已解锁")

t1 = threading.Thread(target=add1)
print("\n");
t2 = threading.Thread(target=add2)

t1.start();t2.start();t1.join();t2.join();
print("---- 主线程执行完成----")
'''
'''
print("---- RLock可重入锁----")
import threading,time
lr = threading.RLock()
def add1():
    lr.acquire()
    print("--la已上锁")
    time.sleep(1)
    lr.acquire()
    print("--lb已上锁")
    # 可重入锁，即使不解锁，也可以多次使用同一个资源
    lr.release()
    print("--lb已解锁")
    lr.release()
    print("--la已解锁")

def add2():
    lr.acquire()
    print("--lb已上锁")
    time.sleep(1)
    lr.acquire()
    print("--la已上锁")
    lr.release()
    print("--lb已解锁")
    lr.release()
    print("--la已解锁")

t1 = threading.Thread(target=add1)
print("\n");
t2 = threading.Thread(target=add2)

t1.start();t2.start();t1.join();t2.join();
print("---- 主线程执行完成----")
'''
#----6.条件变量同步锁----
'''
print("----6.条件变量同步锁(可以等待线程wait()/提醒线程notify()/通知线程notyfyALL()----")
import time,threading,random
# 初始化一个蒸笼
num_list = []
count = 0
# 定义一家包子铺
def producer():
    global num_list,count
    print("----开始生产包子喽")
    while True:
        if lc.acquire():
            num_list.append(1)
            print(f"--{count}.成功生产一个包子")
            lc.notifyAll()
            lc.release()
            time.sleep(random.randint(0,10)*0.1)
            count +=1

def custmers():
    global  num_list,count
    print("----开始吃包子喽")
    while  True:
        if lc.acquire():
            if len(num_list) == 0:
                print("----包子卖完喽")
                lc.wait() #线程闲置，等着吃包子
            num_list.remove(num_list[0])
            print(f"--{count}.消费者吃了一个包子")
            time.sleep(random.randint(1,5)*0.2) # 吃包子花掉的随机时间
            lc.notifyAll()
            lc.release()
            count +=1
# 创建一个条件锁对象
lc = threading.Condition()
t1 = threading.Thread(target=producer)
print("\n");
t2 = threading.Thread(target=custmers)

t2.start();t1.start();t1.join();t2.join();
print("---- 主线程执行完成----")
'''
#----7.停车位进出信号量----
import threading,time,random
# 定义统一时间最高5个线程处于运行状态
semaphore = threading.BoundedSemaphore(5)
def run(ii):
    semaphore.acquire()
    print(f"--{ii}.线程--")
    time.sleep(random.randint(1,5))
    semaphore.release()
for i in range(1,11):
    t = threading.Thread(target=run,args=(i,))
    t.start()


