# usr/bin/python3
# coding:utf-8
'''
author:李浩
2019-7-3:
'''
'''
现有一个数据库记录文件（见附件0005_1.txt），保存了学生课程签到的数据库记录。 内容格式如下 ，
('2017-03-13 11:50:09', 271, 131),
('2017-03-14 10:52:19', 273, 131),
('2017-03-13 11:50:19', 271, 126),
每一行记录保存了学生的一次签到信息。
每一次签到信息的记录，分为三个部分， 分别是签到时间、签到课程的id号、签到学生的id号
要求大家实现下面的函数。其中参数fileName 为 数据库记录文件路径， 输出结果是将数据库记录文件中的学生签到信息保存在一个字典对象中，并作为返回值返回。
def putInfoToDict(fileName):
要求返回的字典对象的格式是这样的：
key 是各个学生的id号， value是 该学生的签到信息
   其中value，里面保存着该学生所有签到的信息
       其中每个签到的信息是字典对象，有两个元素： key 是lessonid的 记录课程id，key是checkintime的 记录签到时间
比如，对于上面的示例中的3条记录，相应的返回结果如下：
{
    131: [
        {'lessonid': 271,'checkintime':'2017-03-13 11:50:09'},
        {'lessonid': 273,'checkintime':'2017-03-14 10:52:19'},
    ],   
    126: [
        {'lessonid': 271,'checkintime':'2017-03-13 11:50:19'},
    ],   
}
'''
fileName1 = "C:\\Users\\Leo\\Desktop\\我的作业\\20190708-id.txt"
def putInofToDict(fileName):
    with open(fileName) as f:
        dic,dic1,dic2 = {},{},{}
        count = 0
        for line in f.read().splitlines():
            ktime = str(str(line).split(",")).split("'")[1]
            kid = int(str(line).split(",")[1])
            sid = int(str(line).split(",")[2].split(')')[0])
            # print(ktime,kid,sid)
            dic1 = {'lessonid':kid,'checkintime':ktime}
            count += 1
            # print(dic1)
            if sid not in dic2:
                dic2[sid] = []
                dic2[sid].append(dic1)
    print(count)
    return dic2
newDic=putInofToDict(fileName1)
print(len(newDic))
import pprint
pprint.pprint(newDic)

