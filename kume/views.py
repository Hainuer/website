# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

from django.shortcuts import render
# 使用Duome模块的Models
from duome.models import Category, Article
#from kume.models import Category, Article

def index(request):
    cat_li = Category.objects.all()
    articles = []
    for cat in cat_li:
        article_li = Article.objects.filter(category=cat).order_by('-pub_date')
        article_li = article_li[:2]
        articles.append(
            { 'category': cat, 'article_li': article_li }
        )
    if not len(articles) > 0:
        articles = None
    ctx_li = {
        'categories': cat_li, 'title': '首页',
        'articles': articles,
    }
    return render(request, 'kume/index.html', ctx_li)

# 阅读文章
def post(request, uuid):
    cat_li = Category.objects.all()
    article = Article.objects.filter(uuid=uuid)[0]
    ctx_li = {
        'categories': cat_li, 'title': article.title,
        'article': article,
    }
    return render(request, 'kume/post.html', ctx_li)

# 列出目录下的文章
def category(request, simple_name):
    cat_li = Category.objects.all()
    ctx_li = { 'categories': cat_li }
    title = simple_name
    try:
        curt_cat = Category.objects.get(simple_name=simple_name)
        if curt_cat:
            article_li = Article.objects.filter(category=curt_cat).order_by('-pub_date')
            title = curt_cat.name
            ctx_li['articles'] = article_li
            ctx_li['curt_cat'] = curt_cat
    except Category.DoesNotExist:
        pass
    ctx_li['title'] = title
    return render(request, 'kume/category.html', ctx_li)

# 列出所有文章
def archive(request):
    cat_li = Category.objects.all()
    article_li = Article.objects.all().order_by('-pub_date')
    ctx_li = {
        'categories': cat_li, 'title': '文档归档',
        'articles': article_li,
    }
    return render(request, 'kume/archive.html', ctx_li)

# 
def about(request):
    cat_li = Category.objects.all()
    ctx_li = {
        'categories': cat_li, 'title': 'About Me',
    }
    return render(request, 'kume/about.html', ctx_li)