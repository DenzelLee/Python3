# coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index1.")

tmplt = u'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>课程信息</title>
</head>
<body>
<form method='POST'>
  <fieldset>
    <legend>添加课程信息:</legend>
    课程名  :  <input type="text"   name="name" value=""><br><br>
    课程描述 :  <textarea    name="desc" value="" ></textarea><br><br>
    显示次序 :  <input type="number"  name="displayidx" value="1"><br><br>
    <input type="submit" value="提交">
  </fieldset>
</form>
<br>
<h2>现有课程</h2>
<table border="1">
<th>课程名</th>
<th>课程描述</th>
<th>显示次序</th>
{% for one in courseList %}
    <tr>
    <td>{{ one.name }}</td>
    <td>{{ one.desc }}</td>
    <td>{{ one.display_idx }}</td>
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
def showadd_course(request):
    # 如果接受到的请求里面有name；就需要添加课程信息到数据库中
    if 'name' in request.POST:
        name = request.POST['name']
        desc = request.POST['desc']
        displayidx = request.POST['displayidx']

        # 注意：数据库里面添加记录的方法，是实例化Model类，传入字段参数值
        # 最后调用save
        course = Course(name=name, desc=desc, display_idx=displayidx)
        course.save()

        # 也可以直接调用object.create方法创建记录
        Course.objects.create(name=name, desc=desc, display_idx=displayidx)

    courseList = Course.objects.all().filter(name__in=[u'数学课', u'语文'])
    ret = template.render({'courseList': courseList})
    return HttpResponse(ret)

















