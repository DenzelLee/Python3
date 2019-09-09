# usr\bin\python3
# coding:utf-8

log1="A girl come in, the name is Jack, level 955;"
log2="A old lady come in, the name is Mary, level 94454"
log3="A pretty boy come in, the name is Patrick, level 194"

# 我的作业：三个方法才写出来，尴尬的一逼！
def getName(log):
    aList=log.split(" ")
    aIndex=aList.index("is")
    aName=aList[aIndex+1]
    aName1=aName.replace(",","")
    print("玩家"+aName1+"已进入游戏！")
    return aName1


# 老师的作业：一个方法就搞定了，确实牛逼！
def getName(log):
     name=log.split("the name is")[1].split(",")[0]
     return name

# 调用方法：
getName(log1)


    
结果:'jack'
