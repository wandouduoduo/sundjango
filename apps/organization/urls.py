# -*- coding: utf-8 -*-
# @Time    : 18/7/19 下午4:49
# @Author  : Sun
# @Version : v1.0
# @File    : urls.py
from .views import *

from django.urls import path, re_path

# 要写上app的名字
app_name = "organization"

# 要写上app的名字
urlpatterns = [
    path('list/', OrgView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name="add_ask"),

    re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name='org_home'),
    re_path('course/(?P<org_id>\d+)/', OrgCourseView.as_view(), name='org_course'),
    re_path('desc/(?P<org_id>\d+)/', OrgDescView.as_view(), name='org_desc'),
    re_path('teacher/(?P<org_id>\d+)/', OrgTeacherView.as_view(), name='org_teacher'),

    path('add_fav/', AddFavView.as_view(), name="add_fav"),

    # 讲师列表
    re_path('teacher/list/', TeacherListView.as_view(), name="teacher_list"),
    # 讲师详情
    re_path('teacher/detail/(?P<teacher_id>\d+)/', TeacherDetailView.as_view(), name="teacher_detail"),
]