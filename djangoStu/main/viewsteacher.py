# coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index1.")

tmplt = u'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>老师信息</title>
</head>
<body>
<form method='POST'>
  <fieldset>
    <legend>添加老师信息:</legend>
    老师名称 :  <input type="text"   name="teachername"       value=""><br><br>
    登录名称 :  <input type="text"   name="loginname"       value=""><br><br>
    描述信息 :  <textarea            name="desc"              value="" ></textarea><br><br>
    展示次序 :  <input type="number" name="displayidx"        value="1"><br><br>
    <select>
    
  <option selected="selected" name="courses" value ="">默認課程</option>
  <option value ="语文课">语文课</option>
  <option value ="数学课">数学课</option>
  <option value ="英语课">英语课</option>
  <option value ="物理课">物理课</option>
    </select>
    <br><br>
    <input type="submit" value="提交">
  </fieldset>
</form>
<br>
<h2>现有老师</h2>
<table border="1">
<th>老师名称</th>
<th>登录名称</th>
<th>描述信息</th>
<th>排序次数</th>
<th>课程管理</th>
{% for one in teacherList %}
    <tr>
    <td>{{ one.teachername }}</td>
    <td>{{ one.loginname }}</td>
    <td>{{ one.desc }}</td>
    <td>{{ one.display_idx }}</td>
    <td>{{ one.courses }}</td>
    </tr>
{% endfor %}
</table>
</body>
</html>
'''
# 导入http模板，通过模板可以直接解析html的内容
from django.template import engines
django_engine = engines['django']
template = django_engine.from_string(tmplt)


# post请求会验证来源，用装饰器csrf_exempt例外来重写方法，绕过csrf跨站脚本攻击检查（正式开发，不能绕过，可以百度解决方法）
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def showadd_teacher(request):
    # 如果接受到的请求里面有name；就需要添加课程信息到数据库中
    if 'teachername' in request.POST:
        teachername = request.POST['teachername']
        loginname = request.POST['loginname']
        desc = request.POST['desc']
        displayidx = request.POST['displayidx']
        # courses = request.POST['courses']

        # 注意：数据库里面添加记录的方法，是实例化Model类，传入字段参数值
        # 最后调用save
        # course = Teacher(teachername=teachername, loginname=loginname, desc=desc, display_idx=displayidx)
        # course.save()

        # 也可以直接调用object.create方法创建记录
        Teacher.objects.create(teachername=teachername, loginname=loginname, desc=desc, display_idx=displayidx)

    teacherList = Teacher.objects.all()
    # teacherList = Course.objects.all().filter(name__in=[u'数学课', u'语文'])
    ret = template.render({'teacherList': teacherList})
    return HttpResponse(ret)

















