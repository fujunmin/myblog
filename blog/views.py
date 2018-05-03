# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
import models

# Create your views here.


# def index(request):
#     return HttpResponse('HELLO word')

# def index(request):
#     return render(request,'blog/index.html',{'hello':'hello blog'})


# def index(request):
#     article = models.Article.objects.get(pk=1)
#     return render(request,'blog/index.html',{'article':article})   # 给前端传递对象


def index(request):
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})   # 给前端传递对象

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_papge(request):

    return render(request,'blog/edit_page.html')

def edit_action(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    models.Article.objects.create(title=title,content=content)
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'article':articles})