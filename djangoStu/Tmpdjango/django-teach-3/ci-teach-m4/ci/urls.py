"""ci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from django.conf.urls.static import static

from main import mgr_course,login_out,mgr_student
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

def ALR(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated():
            return view_func(request, *args, **kwargs)
        return JsonResponse({'retcode': 302, 'redirect':'/login.html'})

    return wrapper




urlpatterns = [

    url(r'^api/login$', login_out.logincheck),
    url(r'^api/logout$', login_out.logoutuser),

    url(r'^api/mgr_course$', ALR(mgr_course.dispatch)),
    url(r'^api/mgr_student', ALR(mgr_student.dispatch) ),
    # url(r'^admin/', admin.site.urls),

] + static('/',document_root='./static')


