from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta, timezone
from model.form import ProfileForm


def hi_wuyuan(request):
    return HttpResponse("hello world!")


def hi_tiger(request):
    context = {}
    context['hello'] = 'hello world'
    context['wuyuan'] = '你好'
    now = datetime.now()
    context['time'] = now  # 强制设置为UTC+8:00
    context['timestamp'] = now.timestamp() * 1000
    return render(request, 'tiger_homepage.html', context)


def upload(request):
    context = {}
    form = ProfileForm
    context['form'] = form
    return render(request, 'upload.html', context)
