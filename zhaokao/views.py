# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

from django.shortcuts import render
from zhaokao.cracker import ZkCracker

# page_active:
# 表示CSS类属性为active的菜单序号
# 依次为0, 2, 4, 8

# 首页
def index(request):
    ctx_dict = {
        'page_title': '首页',
        'items': ZkCracker().indexZhaokao()[1:100],
        'page_active': '0',
        'categories': ZkCracker().listCategory(),
    }
    return render(request, 'zhaokao/index.html', ctx_dict)

# 城市地区分类
def category(request, city_code):
    try:
        crt_page = int(request.GET.get('page'))
    except Exception, e:
        crt_page = 0
    
    if crt_page <= 0:
        crt_page = 1
    category_rtn = ZkCracker().category(city_code, crt_page)
    page_info = category_rtn['page_info']

    # TODO: 硬编码
    url_pre = '/zhaokao/category/' + city_code + '/'

    paginationHtml = getPaginationHtml(page_info, crt_page, url_pre)

    categories = ZkCracker().listCategory()
    page_title = '贵安新区'
    for category in categories:
        if category['city_code'] == city_code:
            page_title = category['city']
        else:
            pass
    for category in category_rtn['jurisdiction']:
        if category['area_code'] == city_code:
            page_title = category['area']
        else:
            pass

    ctx_dict = {
        'page_title': page_title,
        'items': category_rtn['item_li'],
        'pagination_code': paginationHtml,
        'jurisdiction': category_rtn['jurisdiction'],
        'page_active': '2',
        'categories': categories,
    }
    return render(request, 'zhaokao/category.html', ctx_dict)

# 阅读招考资讯
def view(request, link):
    ctx_dict = {
        'page_title': link,
        'item': ZkCracker().viewItem(link),
        'categories': ZkCracker().listCategory(),
        'page_active': '2',
    }
    return render(request, 'zhaokao/view.html', ctx_dict)

# 招聘信息
def want(request):
    ctx_dict = {
        'page_title': '招聘信息',
        'items': ZkCracker().indexZhaopin(),
        'page_active': '4',
        'categories': ZkCracker().listCategory(),
    }
    return render(request, 'zhaokao/want.html', ctx_dict)

#
def notice(request):
    categories = ZkCracker().listCategory()
    ctx_dict = {
        'page_title': '免责声明',
        'page_active': '8',
        'categories': categories,
    }
    return render(request, 'zhaokao/notice.html', ctx_dict)

# 分页代码
def getPaginationHtml(page_info, crt_page, url_pre):
    pages = int(page_info['pages'])
    offset = 2

    html = '<div class="col-lg-12 text-center"><span class="label label-default">共 ' + page_info['pages'] + ' 页 ' + page_info['records'] + ' 条资讯</span><br /><ul class="pagination pagination-sm">'
    if crt_page == 1:
        html += '<li class="disabled"><a href="' + url_pre + '?page=1">首页</a></li>'
    else:
        html += '<li><a href="' + url_pre + '?page=1">首页</a></li>'

    start = crt_page - offset
    end   = crt_page + offset
    for x in xrange(start, end + 1):
        if x <= 0:
            pass
        elif x > 0 and x < crt_page:
            html += '<li><a href="' + url_pre + '?page=' + str(x) + '">' + str(x) + '</a></li>'
        elif x == crt_page:
            html += '<li class="disabled"><a href="' + url_pre + '?page=' + str(x) + '">' + str(x) + '</a></li>'
        elif x > crt_page and x <= pages:
            html += '<li><a href="' + url_pre + '?page=' + str(x) + '">' + str(x) + '</a></li>'
        else:
            pass

    if crt_page == pages:
        html += '<li class="disabled"><a href="' + url_pre + '?page=' + str(pages) + '">尾页</a></li>'
    else:
        html += '<li><a href="' + url_pre + '?page=' + str(pages) + '">尾页</a></li>'
    return html





