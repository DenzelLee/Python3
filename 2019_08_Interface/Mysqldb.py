#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-23 and 20:30
FileName:Mysqldb.py
Description：数据库操作
'''
# 准备工作：D:\TestFiles\InterFace\restapi-teach\backend\project，修改setting——ip地址和端口和账户密码
# 导入数据库包
import MySQLdb
from apiLibrary.apiTest import *
# 实例化类
cm = Course()
# 登录账户
cm.login('auto','sdfsdfsdf')
# 添加数据
cm.add_course(f"数据库测试{nowTime}",f"数据库描述{nowTime}",10)
# 列出数据
clist = cm.list_course(1,20)
print(f"\n当前数据统计：{clist['total']}\n")
for course in clist['retlist'][:]:
    print(course)


print("\n----查询数据库----\n")
# 连接Mysql数据库,ip/用户/密码/库名称/编码
db = MySQLdb.connect("192.168.0.148","songqin","songqin","plesson",charset = 'utf8')

# 获取游标
cursor = db.cursor()
try:
    # 查询数据--查询全部数据
    selectsql = "SELECT * FROM plesson.sq_course;"
    # 查询数据 --统计数据库条数
    totalsql = "SELECT COUNT(*) FROM plesson.sq_course;"
    #
    # # 新增数据--python1
    addsql = f'''INSERT  INTO plesson.sq_course(`NAME`,`DESC`,display_idx) values("python-{nowTime}","pythondecs-{nowTime}",100);'''
    cursor.execute(addsql)
    db.commit()
    # cursor.execute(selectsql)
    #
    # # 修改数据--修改idx为200
    # modifysql = '''UPDATE plesson.sq_course SET display_idx = "200" WHERE display_idx='100';'''
    # cursor.execute(modifysql)
    # db.commit()
    # cursor.execute(selectsql)
    #
    # # 删除数据--删除name=python1的数据
    # delsql = '''DELETE FROM plesson.sq_course WHERE NAME like '测试%';'''
    # cursor.execute(delsql)
    # db.commit()
    cursor.execute(totalsql)
    cursor.execute(selectsql)

    # 大数据循环添加/修改时，需要循环完了再提交，否则每次提交会影响性能，甚至数据库卡死
    db.commit()
except Exception as e:
    print(e)
    # 遇到错误回滚代码
    db.rollback()

# 获取第一条数据
data = cursor.fetchone()
print(f"course onelist:{data}\n")

# 获取指定位置数据
data = cursor.fetchmany(3)
print(f"course manylist:\n{data}\n")

# 获取全部数据
data1 = cursor.fetchall()
for data in data1[:]:
    print(f"course alllist:{data}")


# 关闭数据库，释放资源
db.close()

