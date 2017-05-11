# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
	articles = models.Article.objects.all()
	return render(request, 'myBlog/index.html', {'articles' : articles})

def article(request, id):
	article = models.Article.objects.get(pk=id)
	return render(request, 'myBlog/article.html', {'article' : article})

def edit(request, id):
	if str(id) == '0':
		return render(request, 'myBlog/edit.html')
	article = models.Article.objects.get(pk=id)
	return render(request, 'myBlog/edit.html', {'article' : article})
def editAction(request):
	title = request.POST.get('title')
	content = request.POST.get('content')
	id = request.POST.get('id')
	if id == '0':
		models.Article.objects.create(title=title, content=content)
		articles = models.Article.objects.all()
		return render(request, 'myBlog/index.html', {'articles' : articles})
	article = models.Article.objects.get(pk=id)
	article.title = title
	article.content = content
	article.save()
	return render(request, 'myBlog/article.html', {'article' : article})