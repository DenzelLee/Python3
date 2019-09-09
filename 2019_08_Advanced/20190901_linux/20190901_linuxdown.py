#coding=utf8
'''
Author:leo
Date&Time:2019-09-01 and 17:17
FileName:20190901_linuxdown.py
Description：...
1.编写一个python程序，代码文件名为 memory.py , 该代码文件 计划在远程Linux机器运行。
该程序做如下的事情：
每隔5秒钟 打开文件 /proc/meminfo，该文件包含了系统内存使用信息，前面数行内容如下:
memory.py 程序要将 memFree 、buffers、cached 的值 相加 （结果是可用内存的数量）。
然后除以 MemTotal的值， 得到可用内存占的百分比（赋值给变量 avaMem）。
MemTotal:        1920648 kB
MemFree:           87788 kB
Buffers:          229704 kB
Cached:          1180244 kB
将 avaMem 的数值存入 结果文件ret.txt中。
上面的程序一直运行，每隔 5秒钟 获取记录一次 avaMem 对应的时间戳， 格式如下
20170315_12:10:00  77%
20170315_12:10:05  74%
20170315_12:10:10  70%
20170315_12:10:15  72%

2.再编写一个python程序，代码文件名为 auto.py，该程序运行起来做如下工作：
以自己名字的拼音（比如lixia） 在远程机器建立一个目录 。如果该目录已经存在则跳过此步骤
拷贝文件memory.py 到远程机器该目录下面，
远程在Linux主机执行文件 memory.py
过5分钟后，将远程文件memory.py执行产生的结果文件ret.txt 内容拷贝回本机
'''
import time, datetime,os,subprocess
from pprint import pprint


# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
# piplist = subprocess.check_output("pip list",encoding="utf8")
# print(type(piplist),"\n",piplist)


# ----程序2:上传和下载文件到远程linux服务器
# 导入linux库(linux 安装库：pip install paramiko）
import paramiko
# 创建ssh对象
ssh = paramiko.SSHClient()
# 设置连接方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# 开始连接远程主机(ip,port-默认22可咨询运维,user,password)
ssh.connect("192.168.0.105",22,"root","sdfsdf")
print("----开始工作----")

# 本地文件地址和linux文件地址
windowspath = "D:\MyTest\Python3\Tmp\\2019_08_Advanced\\"
linuxpath = "/root/Desktop/"

# 开始在远程机器上创建个人文件夹
stdin, stdout, stderr = ssh.exec_command(f"cd /root/Desktop;mkdir leo;cd {linuxpath}leo")
print("----个人文件夹创建成功----")
# exec_command返回的是byte类型，需要decode解码
print(stdout.read().decode("utf8"))

# 创建一个客户端， 可以进行文件传输操作
sftp = ssh.open_sftp()
# 将本地的文件传送到远程机器（注意windows和linux的文件分隔号相反的）
sftp.put(f"{windowspath}20190901_LinuxMemory.py", f"{linuxpath}leo/20190901_LinuxMemory.py")
# sftp.put("D:\\360Downloads\python\Python-3.6.5.tgz", f"{linuxpath}leo/Python-3.6.5.tgz")
print("----文件上传成功----")

stdin, stdout, stderr = ssh.exec_command(f"cd {linuxpath}leo;python3 20190901_LinuxMemory.py")
print(stdout.read().decode("utf8"))
print(stderr.read().decode("utf8"))
print("----文件读取成功--")

# 将远程机器的文件下载到本地
sftp.get("/root/Desktop/leo/linuxtime.txt", "./linuxfile.txt")
print("----文件下载成功----")
sftp.close()
ssh.close()

#----方法2：
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
'''




