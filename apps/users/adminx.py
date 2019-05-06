# -*- coding: utf-8 -*-
# @Time    : 18/7/17 下午7:22
# @Author  : Sun
# @Version : v1.0
# @File    : adminx.py
import xadmin

from .models import *

from xadmin import views


class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 修改title
    site_title = '运维后台管理界面'
    # 修改footer
    site_footer = '豌豆多多'
    # 收起菜单
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']
    model_icon = 'fa fa-camera-retro'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']
    model_icon = 'fa fa-comments'


xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(views.CommAdminView,GlobalSettings)