#coding=utf8
'''
Author:leo
Date&Time:2019-09-01 and 17:17
FileName:20190901_memory.py
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

# ----程序1
# 导入linux库
import paramiko
# 创建ssh对象
ssh = paramiko.SSHClient()
# 设置连接方式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# 开始连接远程主机(ip,port-默认22可咨询运维,user,password)
ssh.connect("192.168.0.148",22,"root","sdfsdf")
print("----开始工作----")

# 每5秒钟获取一次服务器剩余可用内存（memFree 、buffers、cached之和）
count = 1
while True:
    # 获取开始时间
    starttime = datetime.datetime.now()
    time.sleep(5)
    # 获取结束时间
    endtime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # 开始执行命令
    stdin,stdout,stderr = ssh.exec_command("cd /proc;cat meminfo")
    # 切割日志内容，获取前4个剩余内存的int数据
    res = str(stdout.read().decode("utf8")).split("SwapCached:            0 kB")[0]
    # print(res.split("\n"))
    sum = 0
    slist = []
    # 获取前4个内存数据，累加后三个除以第一个总内存，得出剩余内存使用率
    for i in res.split("\n")[0:-1]:
        slist.append(int(i.split(":")[1].split(" kB")[0].strip()))
        if res.split("\n")[0:-1].index(i)>0:
            sum +=int(i.split(":")[1].split(" kB")[0].strip())
    # 打印结束日期和剩余内容使用率（百分制%）
    avaMem = f"{endtime} {sum/slist[0]:.2%}\n"
    print(avaMem)
    # 每5秒记录一次，追加到txt文件中
    with open("linuxtime.txt", "a", encoding="utf8") as t:
        t.write(avaMem)
    count += 1
    with open("linuxtime.txt", "r", encoding="utf8") as t1:
        print(f"成功记录次数统计：{len(t1.readlines())}次")
    print(f"{count}.----计算成功----")

    # 防止死循环
    if count >10:
        break

# ----方法2：
'''
import time, datetime

# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

# memory.py
memDict = {
    "MemFree":[],
    "Buffers":[],
    "Cache":[],
    "MemTotal":[],
    "avaMem":[],
}
# 处理单行信息 类似-->
# 获取具体数值，写入字典当中
def handleStrline(strLine):
    for keys in memDict: # 循环字典
        if strLine.startwith(keys): # 获取需要的数据
            # 根据：对字符串进行分割，dataValue 得到的格式类似于
            dataValue = strLine.split(":")[1]
            # 去掉首位的空格和字母
            dataValue = dataValue.strip(" kB")
            # 把数据写入字典，追加到对应的列表的末尾
            memDict[keys].append(int(dataValue))
'''
# ----方法3
'''
# 读取 /proc/meminfo
def reaMeminfo():
    for strLine in open("/proc/meminfo","r",encoding="utf8"):
        # 读一行，处理一行
        handleStrline(strLine)

for i in range(5):
    # 从文件中获取 memfree buffers cached memtotal,写入字典
    reaMeminfo()
    # 计算百分比
    avaMem = (memDict["MemFree"][i]+memDict["Buffers"][i]+memDict["Cache"][i])/memDict["Cache"][i]
    # 四舍五入
    avaMem = round(avaMem*100)
    # 处理成日期格式化和百分比
    avaMem = time.strftime("%Y%m%d_%H:%M:%S") +"    "+ str(avaMem)+"%"
    # 内存百分比加入字典
    memDict["avaMem"].append(avaMem)
    time.sleep(5)

for keys in memDict:
    print(keys,memDict[keys])

# 结果写入ret.txt
with open("./ret.txt","w",encoding="utf8") as f:
    for values in memDict["avaMem"]:
        f.write(values+"\n")
'''
