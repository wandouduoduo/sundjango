"""sundjango URL Configuration

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
# from django.contrib import admin
from django.urls import path, include, re_path
import xadmin
from sundjango.settings import MEDIA_ROOT
from django.views.static import serve
from django.views.generic import TemplateView

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView, IndexView
from organization.views import OrgView
# 函数方法
# from users import views

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name='index'),


    # 用户
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('login/', views.user_login, name='login'),
    path('captcha/', include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    path('forget/',ForgetPwdView.as_view(), name='forget_pwd'),
    re_path(r'reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),

    # 个人信息
    path("users/", include('users.urls', namespace="users")),

    # 课程
    path("course/", include('course.urls', namespace="course")),

    # 机构
    path("org/", include('organization.urls', namespace="org")),
    # path('org_list/', OrgView.as_view(), name='org_list'),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # 静态文件
    # re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT }),

    # 富文本编辑器url
    path('ueditor/',include('DjangoUeditor.urls' )),
]

# 全局404页面配置
handler404 = 'users.views.pag_not_found'

# 全局500页面配置
handler500 = 'users.views.page_error'
