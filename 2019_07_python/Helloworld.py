# usr/bin/python3
# coding:utf-8
'''

2019-7-3:
'''


def putInfoToDict(fileName):
    retDict = {}
    with open(fileName) as f:
        lines = f.read().splitlines()
        count = 0
        for line in lines:
            # remove '(' and ')'
            line = line.replace('(', '').replace(')', '').replace(';', '').strip()

            parts = line.split(',')
            ciTime = parts[0].strip().replace("'", '')
            lessonid = int(parts[1].strip())

            userid = int(parts[2].strip())

            toAdd = {'lessonid': lessonid, 'checkintime': ciTime}
            count += 1
            # if not in, need to create list first
            if userid not in retDict:
                retDict[userid] = []
            retDict[userid].append(toAdd)

            # or just
            # retDict.setdefault(userid,[]).append(toAdd)
    print(count)
    return retDict


ret = putInfoToDict("C:\\Users\\Leo\\Desktop\\我的作业\\20190708-id.txt")
print(len(ret))
import pprint

pprint.pprint(ret)


