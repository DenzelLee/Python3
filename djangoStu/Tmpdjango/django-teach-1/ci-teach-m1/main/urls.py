from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^show$', views.show_all_students),
    url(r'^show2$', views.show_all_students2),
]