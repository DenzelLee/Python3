#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-03 and 16:32
FileName:20190903_格式化服务器聊天.py
Description：...
实现  一个 简单的 客服聊天系统。
客服中心是tcp服务端程序   客户使用tcp客户端程序。
服务端程序 先运行， 绑定本机一个ip地址， 等待客户端系统连接上来 。
客户端程序有一个命令行参数， 表示客户的名字
连接成功后，  客户端发送给服务端第一个消息 必须告诉客服中心，用户的名字
一个客户连接后，别的客户不能连接， 等到前面的客户断开连接后，才能连上。
客户端和服务端都是手动在终端输入信息，发送消息后，必须等待接受到对方的消息才能发送下一个消息。
我们定义消息的格式如下：
0008|1|nickname
用竖线隔开3部分的字段，分别表示 消息长度、 消息类型 、消息内容
前面字段是4个字节的字符串，比如'0008'，其内容是数字，表示消息的长度， 不足4个字节前面补零。
注意长度是整个消息内容的长度，包括  消息头部和消息体
后面用竖线隔开的字段，是1个字节的字符串，是消息类型，其内容是数字，1表示客户昵称， 2 表示 普通消息
前面两个字段合起来 0008|1|  ， 可以看成是一个消息的头部， nickname 是消息体
再后面用竖线隔开的字段是 消息内容，其长度等于 前面消息长度字段指明的长度 减去 消息头部长度 （也就是7个字节）
'''
# ----方法2：

# coding=utf8
import sys,time, datetime
from socket import socket,AF_INET,SOCK_STREAM

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

host = '127.0.0.1'
port = 21567
bufsize = 1024
addr = (host, port)

class CloseSocketError(Exception):
    pass

# 一个 ConnectionHandler 处理和一个客户端的连接
class ConnectionHandler():

    # 格式化输出消息头：0008|1|nickname
    LEN_MSG_LEN_FIELD = 4
    LEN_MSG_LEN_TYPE_FIELD = 7

    def __init__(self,sock):
        # 消息缓存区
        self._readbuffer = b''
        self.sock = sock
        self.customername = ''

    # msgBody 是 unicode
    @staticmethod
    def encode(msgType, msgBody):
        rawMsgBody = msgBody.encode('utf8')

        msgLenth = '{:04}' \
        .format(len(rawMsgBody)+ConnectionHandler.LEN_MSG_LEN_TYPE_FIELD) \
        .encode()

        msgType = f'{msgType}'.encode()
        return b'|'.join([msgLenth,msgType,rawMsgBody])

    @staticmethod
    def decode(rawmsg):
        msgType = int(rawmsg[5:6])  # 这样写rawmsg[5] 返回的是字节对应的数字
        msgbody = rawmsg[ConnectionHandler.LEN_MSG_LEN_TYPE_FIELD:].decode('utf8')
        return [msgType,msgbody]

    def readMsg(self):
        bytes = self.sock.recv(bufsize)

        # ** 用不同的返回值表示不同的含义

        # 当对方关闭连接的时候，抛出异常
        if not bytes:
            self.sock.close()
            raise CloseSocketError()

        # 应用程序的读取缓冲，和前面讲的系统的读取缓冲是两个不同的缓冲
        self._readbuffer += bytes

        buffLen = len(self._readbuffer)

        # 如果已经获取了消息头部 (包括 消息长度，消息类型)
        if buffLen >= self.LEN_MSG_LEN_TYPE_FIELD:
            msgLen = int(self._readbuffer[:self.LEN_MSG_LEN_FIELD])
            # 缓存区消息 已经包含了一个整体的消息(包括 消息长度，消息类型，消息体)
            if buffLen >= msgLen:
                # 从缓存区，截取整个消息
                msg = self._readbuffer[0:msgLen]
                # 缓存区变成剩余的消息部分
                self._readbuffer = self._readbuffer[msgLen:]
                return self.decode(msg)
        # 如果已经获取的消息还不包括一个完整的消息头部, 不做处理等待下面继续接受消息
        else:
            return None
        print('get:%s' % bytes)

    # msgBody 是 unicode
    def sendMsg(self,msgType,msgBody):
        self.sock.sendall(self.encode(msgType,msgBody))

    def handleMsg(self,msgType,msgBody):
        # 客户名称
        if msgType == 1:
            self.customername = msgBody
            print('\n---- 客户名称为：%s' % self.customername)

        # 普通消息
        elif msgType == 2:
            print(msgBody)
            print('---------------')
            # 客服输入消息内容
            msgSend = input('客户回复 >>>')
            self.sendMsg(2,msgSend)

    # 主循环，不断的接受消息发送消息
    def mainloop(self):
        while True:
            try:
                msg = self.readMsg()
                # msg 里面包含了 type 和body
                if msg:
                    msgType,msgBody= msg
                    self.handleMsg(msgType,msgBody)
            except CloseSocketError:
                print('对方断开了连接,等待下一个客户')
                break
            except IOError:
                print('对方断开了连接,等待下一个客户')
                break
#创建socket，指明协议
tcpSerSock = socket(AF_INET, SOCK_STREAM)

#绑定地址和端口
tcpSerSock.bind(addr)

tcpSerSock.listen(5)

print('\n---- 1.服务器启动成功：等待客户端连接... ----')
while True:
    #阻塞式等待连接请求
    tcpCliSock, addr = tcpSerSock.accept()
    print('\n---- 2.客户连接成功，用户ip信息:', str(addr))

    handler = ConnectionHandler(tcpCliSock)
    handler.mainloop()

tcpSerSock.close()
