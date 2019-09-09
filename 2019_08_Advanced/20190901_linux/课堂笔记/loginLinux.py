# -*- coding: utf-8 -*-
#   __author__:lenovo
#   2019/9/1

import paramiko

# 创建 ssh 对象
ssh = paramiko.SSHClient()

# 设置连接方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())



# 开始连接远程主机 (IP地址， 端口号，用户名， 密码)
ssh.connect("192.168.2.106", 22, "root", "sdfsdf")



# # 开始在远程机器上执行命令
# stdin, stdout, stderr = ssh.exec_command("cd /root/Desktop;rm test.py")
# print(stdout.read().decode("utf8"))

# 创建一个客户端， 可以进行文件传输操作
sftp = ssh.open_sftp()

# # 将本地的文件传送到远程机器
# sftp.put("D:\\test\script\\test\picture.png", "/root/Desktop/picture.png")

# 将远程机器的文件下载到本地
sftp.get("/root/Desktop/test.py", "D:\\test\script\study\day5\\test1.py")

sftp.close()
ssh.close()
