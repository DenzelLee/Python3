# coding=utf8
from __future__ import unicode_literals
from django.db import models

# 创建本地数据库信息表，用于存储数据信息，修改models配置信息后，需要进入根目录执行下列两个命令：
# python manage.py makemigrations main  --加载新内容
# python manage.py migrate  --  确认加载信息

# Create your models here.
# 课程表
class Course(models.Model):
    # 课程名
    name = models.CharField(max_length=100)
    # 课程描述
    desc = models.CharField(max_length=1000, null=True, blank=True)
    # 展示优先级
    display_idx = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "main_course"
# 老师表
class Teacher(models.Model):
    # 老师姓名
    teachername = models.CharField(max_length=100)
    # 登录名称
    loginname = models.CharField(max_length=100)
    # 老师描述
    desc = models.CharField(max_length=1000, null=True, blank=True)
    # 展示优先级
    display_idx = models.PositiveSmallIntegerField(default=0)
    # 课程信息
    # courses = models.ManyToManyField(Course, related_name='course_teacher')

    class Meta:
        db_table = "main_teacher"