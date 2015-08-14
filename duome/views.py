# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from duome.models import Article, Category, Mumbler

# activate_menu
# 显示当前激活的菜单
# 说明: 
#  0: index
#  2: category
#  4: mumbler
#  8: archive
# 16: about

# 首页视图
def index(request):
    articles = Article.objects.all().order_by('-pub_date')[:10]
    categories = Category.objects.all()
    ctx_dict = {
        'articles': articles, 
        'title': '首页',
        'categories': categories,
        'activate_menu': '0',
    }
    return render(request, 'duome/index.html', ctx_dict)

# Mumbler
def mumbler(request):
    categories = Category.objects.all()
    mumblers = Mumbler.objects.all().order_by('-pub_date')
    paginator = Paginator(mumblers, 5)
    # 分页
    page = request.GET.get('page')
    try:
        mumblers = paginator.page(page)
    except PageNotAnInteger:
        mumblers = paginator.page(1)
    except EmptyPage:
        mumblers = paginator.page(paginator.num_pages)
    
    for idx in range(0, len(categories)):
         categories[idx].nums = len(Article.objects.filter(category=categories[idx]))
    top_articles = Article.objects.all().order_by('-views')[:10]
        
    ctx_dict = {
        'categories': categories, 
        'activate_menu': '4',
        'title': '碎碎念',
        'mumblers': mumblers,
        'top_articles': top_articles,
    }
           
    return render(request, 'duome/mumbler.html', ctx_dict)
    
# Category
def category(request, simple_name):
    categories = Category.objects.all()
    title = simple_name
    
    for idx in range(0, len(categories)):
         categories[idx].nums = len(Article.objects.filter(category=categories[idx]))
    top_articles = Article.objects.all().order_by('-views')[:10]
    ctx_dict = {
        'categories': categories, 
        'activate_menu': '2',
        'top_articles': top_articles,
    }
    try:
        curt_category = Category.objects.get(simple_name=simple_name)
        if curt_category:
            articles = Article.objects.filter(category=curt_category).order_by('-pub_date')
            paginator = Paginator(articles, 5)
            # 分页
            page = request.GET.get('page')
            try:
                articles = paginator.page(page)
            except PageNotAnInteger:
                articles = paginator.page(1)
            except EmptyPage:
                articles = paginator.page(paginator.num_pages)
           
            ctx_dict['articles'] = articles
            ctx_dict['curt_category'] = curt_category
            title = curt_category.name
    except Category.DoesNotExist:
        pass
    
    ctx_dict['title'] = title
    return render(request, 'duome/category.html', ctx_dict)
    

# 阅读博客
def post(request, uuid):
    categories = Category.objects.all()
    try:
        article = Article.objects.filter(uuid=uuid)[0]
        article.views = article.views + 1
        article.save()
        title = article.title
    except Exception:
        article = None
        title = uuid
    
    for idx in range(0, len(categories)):
         categories[idx].nums = len(Article.objects.filter(category=categories[idx]))
    top_articles = Article.objects.all().order_by('-views')[:10]
    ctx_dict = {
        'categories': categories, 
        'title': title,
        'activate_menu': '2',
        'article': article,
        'top_articles': top_articles,
    }
    return render(request, 'duome/post.html', ctx_dict)

# 博客归档
def archive(request):
    categories = Category.objects.all()
    for idx in range(0, len(categories)):
         categories[idx].nums = len(Article.objects.filter(category=categories[idx]))
    top_articles = Article.objects.all().order_by('-views')[:10]
    
    articles = Article.objects.all().order_by('-pub_date')
    ctx_dict = {
        'categories': categories, 
        'title': '文章归档',
        'activate_menu': '8',
        'articles': articles,
        'top_articles': top_articles,
    }
    return render(request, 'duome/archive.html', ctx_dict)

# 关于页面
def about(request):
    categories = Category.objects.all()
    ctx_dict = {
        'categories': categories, 
        'title': 'About',
        'activate_menu': '16',
    }
    return render(request, 'duome/about.html', ctx_dict)

