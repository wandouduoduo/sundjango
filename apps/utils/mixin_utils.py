# -*- coding: utf-8 -*-
# @Time    : 18/7/25 下午9:16
# @Author  : Sun
# @Version : v1.0
# @File    : mixin_utils.py
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self,request,*args,**kwargs):
        return super(LoginRequiredMixin, self).dispatch(request,*args,**kwargs)