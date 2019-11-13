HOST   = '192.168.1.104'   # '192.168.0.103'
PORT   = 22
USER   = 'stt5'
PASSWD = 'stt5200'
PACKAGE_DIR = r'f:\tmp\restapi-teach.zip'

import paramiko
import sys

#创建SSHClient 实例对象
ssh = paramiko.SSHClient()

#调用方法，表示没有存储远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接远程机器  地址、端口、用户名密码
ssh.connect(HOST,PORT,USER, PASSWD)


def remoteRun(cmd, printOutput=True):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.read().decode('utf8')
    errinfo = stderr.read().decode()
    if printOutput:
        print(output+errinfo)
    return output+errinfo

# ------------------------------
#检查是否有先前的版本运行
print('检查是否有先前的版本运行')
output = remoteRun('ps -ef|grep apiteach|grep -v grep')


# 如果存在，则杀死进程
if 'python3 project/cherrypy_startup.py apiteach' in output:
    print('服务运行中，停止服务...')

    #获取进程id
    parts = output.split(' ')

    parts = [part for part in parts if part]

    pid = parts[1]

    # 杀死进程
    output = remoteRun(f'kill -9 {pid}' )

    #再次检查是否有先前的版本运行
    output = remoteRun('ps -ef|grep apiteach|grep -v grep')
    if 'python3 project/cherrypy_startup.py apiteach' in output:
        print('不能停止运行的服务！！！')
        # 退出进程
        sys.exit(3)

    else:
        print('停止成功')



print('删除原来的代码包')
remoteRun('rm -f restapi-teach.zip')


print('上传安装包')
sftp = ssh.open_sftp()
sftp.put(PACKAGE_DIR, '/home/stt5/restapi-teach.zip')
sftp.close()



print('备份原来的安装目录')
remoteRun('rm -rf restapi-teach.bak;mv restapi-teach restapi-teach.bak')


print('解压安装包...',end='')
remoteRun('unzip restapi-teach.zip',printOutput=False)
print('ok')


print('运行')
remoteRun('cd restapi-teach;chmod +x run.sh;dos2unix run.sh; ./run.sh;sleep 5')


print('检查是否运行成功')
output = remoteRun('ps -ef|grep apiteach|grep -v grep')

# 如果存在，运行成功
if 'python3 project/cherrypy_startup.py apiteach' in output:
    print('新版本服务运行成功')
else:
    print('新版本服务没有运行！！')
    sys.exit(3)

# # 防火墙打开8066端口
# remoteRun('iptables -I INPUT -p TCP --dport 8066 -j ACCEPT;/sbin/service iptables save')



from selenium import webdriver

driver= webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(f'http://{HOST}:8066/mgr/login/login.html')

driver.find_element_by_id('username').send_keys('auto')
driver.find_element_by_id('password').send_keys('sdfsdfsdf')
driver.find_element_by_tag_name('button').click()


input('...')

