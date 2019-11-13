"""djangoStu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 导入应用，main-application
from django.contrib import admin

# 导入子路由，main-application的urls.py里面的子url路由
from django.conf.urls import url, include

# 导入静态文件
from django.conf.urls.static import static

# 导入main-application的views视图
from main import views
from main import viewsteacher

urlpatterns = [
    url('admin/', admin.site.urls),  # django管理系统登录页面（内置）
    # path('main/', include('main.urls')),  # main应用里分级文件inlude.url的子路由
    url(r'^showadd_course$', views.showadd_course),
    url(r'^showadd_teacher$', viewsteacher.showadd_teacher),

# 静态文static的子路由,访问方式：http://127.0.0.1:8001/static/chengdu.html
] + static('/static', document_root='./static')