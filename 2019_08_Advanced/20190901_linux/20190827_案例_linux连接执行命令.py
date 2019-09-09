#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-09-01 and 18:01
FileName:20190827_案例_linux连接执行命令.py
Description：...
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))


import paramiko

# 创建 ssh 对象
ssh = paramiko.SSHClient()

# 设置连接方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 开始连接远程主机 (IP地址， 端口号，用户名， 密码)
ssh.connect("192.168.0.105", 22, "root", "sdfsdf")

# 开始在远程机器上执行命令
# stdin, stdout, stderr = ssh.exec_command("cd /root/Desktop;vim test.py")
stdin, stdout, stderr = ssh.exec_command("ifconfig")
print(stdout.read().decode("utf8"))

# 创建一个客户端， 可以进行文件传输操作
# sftp = ssh.open_sftp()

# # 将本地的文件传送到远程机器
# sftp.put("D:\\test\script\\test\picture.png", "/root/Desktop/picture.png")

# # 将远程机器的文件下载到本地
# sftp.get("./test.py", "./test1.py")

# sftp.close()
ssh.close()
