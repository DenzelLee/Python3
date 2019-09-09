#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
'''
Author:leo
Date&Time:2019-08-28 and 12:36
FileName:20190828_FFmpeg多媒体框架.py
Description：...
前言：
1.录制视频：
Ⅰ：ffmpeg.exe -y -rtbufsize 100M -f gdigrab -framerate 10 -draw_mouse 1 -i desktop
-c:v libx264 -r 20 -crf 35 -pix_fmt yuv420p -fs 100M "需要保存在本地的文件名"
Ⅱ：退出-录制过程中，用户按键盘“q”，可以退出
2.合并视频
ffmpeg.exe -f concat -i concat.txt -codec copy out.mp4
其中concat.txt 是要合并视频的文件列表。格式如下，每行以file 开头 后面是要合并的视频文件名：
file 20170330_110818.mp4
file 20170330_110833.mp4

'''
import time
import os
import glob
import subprocess
import datetime
# 获取当前格式化-年月日：时分秒
nowTimee = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# 获取当前格式化-年月日：时分秒
nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

# 获取工具路径
syspath = "D:\\TestFiles\\ffmpeg\\bin\\ffmpeg.exe"
filepath = "D:\\TestFiles\\ffmpeg\\bin\\"

# 录制函数
def recoding():

    # 获取当前格式化-年月日：时分秒
    nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

    # 输出文件名
    outfile = f'{nowTime}' + '.mp4'
    rcmd = filepath + "ffmpeg.exe -y -rtbufsize 100M -f gdigrab -framerate 10 " \
                 "-draw_mouse 1 -i desktop -c:v libx264 -r 20 -crf 35 -pix_fmt " \
                 "yuv420p -fs 100M "+ filepath + outfile

    print("----1.开始录制----")
    os.system(rcmd)

    # 怎么录制5秒自动退出?
    # time.sleep(5)
    # os.system("q")

# 合并函数
def merging():

    # 获取当前格式化-年月日：时分秒
    nowTime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))

    # 切换都目录文件，进入文件执行命令，可以避开命令中包含中文，导致报错
    os.chdir(filepath)
    # 查看当前目录，是否切换成功
    print("成功进入目录，当前路径为：",os.system("cd"))

    # # 1.正则匹配获取目录下的文件列表
    filelist = glob.glob(filepath+'*.mp4')

    # 2.OS方法获取目录下的文件列表
    # filelist = os.listdir(filepath)
    # count =0
    # for ipath in filelist:
    #     if not ipath.endswith(".mp4"):
    #         filelist.remove(filelist[count])
    #         continue
    #     count +=1
    # print("清除非MP4文件以后目录如下：\n",filelist)

    filelist1 = []
    if filelist:
        print("\n----2.当前目录视频文件为：\n")

        # 当前目录视频列表
        for name in filelist:
            print(int(filelist.index(name))+1, "-", name.split(filepath)[1])

        # 用户输入需要合并的数目
        strlist = ",".join([str(idx+1) for idx in range(len(filelist))])
        numlist = input(f"\n请输入你要合并的文件：(以逗号分隔，比如 {strlist}...)").split(",")

        print(f"\n输入统计total：{len(list(numlist))}",numlist,"\n本地统计total：{len(filelist)}",filelist,"\n")

        # 如果输入数目大于当前条数，退出并提示
        if len(numlist) <= len(filelist):
            for num in numlist:
                filelist1.append(int(num)-1)
            try:
                with open("concat.txt", "w",encoding="utf8") as f:
                    for i in filelist1:
                        f.write("file"+" "+filelist[i].split(filepath)[1]+"\n")
                mcmd = f"ffmpeg.exe -f concat -i concat.txt -codec copy {nowTime}_outfile.mp4"
                os.system(mcmd)
                print("\n----视频合并完成，新名称为：", [os.path.basename(one) for one in filelist][-1])
            except Exception as e:
                print("\n视频合成异常：",e)
        else:
            print("\n----不好意思，输入内容有误，请重新开始游戏！")
    else:
        print("\n----2.当前目录视频文件为空：", filelist)

tag = True
while tag == True:
    info = input("\n开始游戏，请输入您的数字：1--录制视频。2--合并视频。3--退出游戏(quit)：")
    if info == "1":
        recoding()
    elif info == "2":
        merging()
    elif info =="quit":
        tag = False
        print("\n----谢谢参与，成功退出游戏！----\n")
    else:
        info = input("\n----您的输入有误，请重新输入!1--录制视频。2--合并视频。3--退出游戏(quit)：")


# ----方法2：
# import datetime, os
# ffmpegPath = "D:\desktop\songqin\python进阶\day2\\ffmpeg-20190219-ff03418-win64-static\\bin"
# outPath = "D:\desktop\songqin\python进阶\day2\\test"
# def recording():
#     videoName = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#
#     cmdStr = ffmpegPath + """\\ffmpeg.exe -y -rtbufsize 100M -f gdigrab -framerate 10 -draw_mouse 1 -i desktop -c:v libx264 -r 20 -crf 35 -pix_fmt yuv420p -fs 100M "%s\%s.mp4" """ %(outPath, videoName)
#     print(cmdStr)
#
#     os.system(cmdStr)
#
#
# def merging():
#     # 获取目录下的文件列表
#     fileSli = os.listdir(outPath)
#     # 把不是MP4的文件剥离出去
#     idx = 0
#     for i in fileSli:
#         if not i.endswith(".mp4"):
#             fileSli.remove(fileSli[idx])
#             continue
#         idx += 1
#
#     # 如果文件为空， 则结束运行
#     if not fileSli:
#         print("目录中没有mp4文件")
#         return
#     # 列表排序
#     fileSli.sort()
#     # 打印视频文件列表
#     idx = 0
#     for i in fileSli:
#         print(idx, i)
#         idx += 1
#
#     # 选择需要操作的文件序号
#     chooseNum = input("请选择需要合并的视频文件（格式 1,2,3）")
#     chooseSli = chooseNum.split(",")
#
#     # 操作 concat.txt 文件
#     with open(outPath+"\concat.txt", "w", encoding="utf8") as f:
#         for i in chooseSli:
#             f.write("file " + fileSli[int(i)] + "\n")
#
#
#     os.chdir(outPath)
#     os.system("cd")
#     cmdStr = ffmpegPath + "\\ffmpeg.exe -f concat -i concat.txt -codec copy out.mp4"
#     print(cmdStr)
#     os.system(cmdStr)
#
# while True:
#     chooseInput = input("请选择需要做的操作：1、录制视频；2、合并视频")
#
#     if chooseInput == "1":
#         recording()
#     elif chooseInput == "2":
#         merging()
#     elif chooseInput == "exit":
#         break
#     else:
#         print("非法输入")


# ----方法3：
# # coding=utf8
# import time,os
# import glob
#
# FFMPEG_PATH = 'D:\\TestFiles\\ffmpeg\\bin\\ffmpeg.exe'
# VIDEO_DIR  = 'D:\\TestFiles\\ffmpeg\\bin\\'
#
#
# def recording():
#     # 输出视频文件
#     outputfile = VIDEO_DIR  + time.strftime('%Y%m%d_%H%M%S', time.localtime()) + '.mp4'
#
#     # 工具目录
#
#     settings = '-y -rtbufsize 100M -f gdigrab -framerate 20 ' +\
#                '-draw_mouse 1 -i desktop -c:v libx264 -r 20 ' +\
#                '-crf 35 -pix_fmt yuv420p ' \
#                '-fs 100M   "%s"' % outputfile
#
#
#     recordingCmdLine = FFMPEG_PATH + ' ' + settings
#
#     # 查看命令内容
#     print(recordingCmdLine)
#
#     # 执行命令录制视频
#     os.system(recordingCmdLine)
#
#
# def merging():
#
#     os.chdir(VIDEO_DIR)
#     fileList = glob.glob(VIDEO_DIR + '*.mp4')
#     fileList =  [os.path.basename(one) for one in fileList]
#
#
#     if fileList:
#         print('\n目录中有这些视频文件：')
#     else:
#         print('\n目录中没有视频文件')
#         return
#
#     idx = 1
#     for one in fileList:
#         print('%s - %s' % (idx, one))
#         idx += 1
#
#     print('\n请选择要合并视频的视频文件序号(格式 1,2,3,4) :', end=' ')
#
#     mergeSequence = input('')
#     videoFilesToMer = mergeSequence.split(',')
#     videoFileNamesToMer = [fileList[int(one.strip())-1] for one in videoFilesToMer]
#
#     print(videoFileNamesToMer)
#
#     with open('concat.txt','w',encoding='utf8') as f:
#         for one in videoFileNamesToMer:
#             f.write('file ' + one + '\n')
#
#
#     cmd = FFMPEG_PATH + ' -f concat -i concat.txt -codec copy out.mp4'
#     # 执行命令录制视频
#     os.system(cmd)
#
# while True:
#     print('\n请选择您要做的操作：1-录制视频，2-合并视频 :', end=' ')
#     choice = input('')
#     if choice == '1':
#         recording()
#     elif choice == '2':
#         merging()