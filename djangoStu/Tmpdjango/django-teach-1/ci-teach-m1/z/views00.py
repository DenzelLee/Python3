# coding=utf8
from django.shortcuts import render


from django.http import HttpResponse

def show_all_students(request):
    response2 = u'''
        <!DOCTYPE html>
        <html><head><meta charset="UTF-8"></head>
        <body>张三，李四</body></html>
        '''
    return HttpResponse(response2)




def show_all_students2(request):
    response2 = u'''
    <!DOCTYPE html>
    <html><head><meta charset="UTF-8"></head>
    <body>张三，李四</body></html>
    '''
    return HttpResponse(response2)




def check_exist(request):
    print request.GET
    loginname = request.GET['loginname']
    age  = int(request.GET['age'])
    if loginname not in studentTable:
        return HttpResponse(u'没有这个学生')

    student = studentTable[loginname]
    if student['age'] != age:
        return HttpResponse(u'没有这个学生')

    return HttpResponse(u'有这个学生')
