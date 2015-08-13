# -*- coding: utf-8 -*-
__author__ = 'Phoenix'

import re
import sys
import requests
from bs4 import BeautifulSoup

class ZkCracker:
    def  __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.site = 'http://www.xinguizhou.com'

    #
    def category(self, city_code, page_idx):
        url = self.site + '/zhaokao/' + city_code + '/list_' + str(page_idx) + '.html'
        soup = self.getSoup(self.getRequest(url))
        # 资讯列表
        item_li = []
        idx = 0
        for li in soup.find('ul', attrs = {'class': 'd2 ico2'}).find_all('li'):
            a_li = li.find_all('a')
            idx = idx + 1
            link = a_li[1].get('href')
            link = link.replace('/', '-')[1:]
            item_li.append({
                'idx': idx,
                'title': a_li[1].get('title'),
                'url': self.site + '/' + link,
                'link': link,
                'city': a_li[0].get_text(),
                'city_code': self.site + a_li[0].get('href'),
                'up_date': li.find('span').get_text()
            })
        # 页数等基础信息
        page_info_li = re.findall(r'\d+', soup.find('ul', attrs={'class': 'pagelist'}).find_all('li')[-1].get_text())
        if len(page_info_li) == 2:
            page_info = {'pages': page_info_li[0], 'records': page_info_li[1]}
        # 所辖地区
        jurisdiction = []
        dl = soup.find('dl', attrs={'class': 'tbox_xian'})
        if dl:
            for a in dl.find('ul').find_all('a'):
                jurisdiction.append({
                    'area': a.get_text(),
                    'area_code': a.get('href').replace('zhaokao', '').replace('/', '')
                })
        return {'item_li': item_li, 'page_info': page_info, 'jurisdiction': jurisdiction}

    #
    def listCategory(self):
        soup = self.getSoup(self.getRequest(self.site))
        rtn_li = []
        for a in soup.find('div', attrs={'class': 'tags'}).find_all('a')[0:-1]:
            rtn_li.append({
                'city': a.get_text(),
                'city_code': a.get('href').replace('zhaokao', '').replace('/', '')
            })
        return rtn_li


    def indexZhaokao(self):
        # 资讯列表
        item_li = []
        soup = self.getSoup(self.getRequest(self.site))
        idx = 0
        for li in soup.find('ul', attrs = {'class': 'd2 ico2'}).find_all('li'):
            a_li = li.find_all('a')
            idx = idx + 1
            link = a_li[1].get('href')
            link = link.replace('/', '-')[1:]
            item_li.append({
                'idx': idx,
                'title': a_li[1].get('title'),
                'url': self.site + link,
                'link': link,
                'city': a_li[0].get_text(),
                'city_code': self.site + a_li[0].get('href'),
                'up_date': li.find('span').get_text()
            })
        return item_li


    #
    def indexZhaopin(self):
        # 资讯列表
        item_li = []
        soup = self.getSoup(self.getRequest(self.site))
        idx = 0
        for li in soup.find_all('ul', attrs = {'class': 'd2 ico2'})[2].find_all('li'):
            a = li.find('a')
            idx = idx + 1
            link = a.get('href')
            link = link.replace('/', '-')[1:]
            item_li.append({
                'idx': idx,
                'title': a.get('title'),
                'url': self.site + link,
                'link': link,
                'up_date': li.find('span').get_text()
            })
        return item_li


    #
    def viewItem(self, link):
        link = 'http://www.xinguizhou.com/' + link.replace('-', '/')
        soup = self.getSoup(self.getRequest(link))
        rtn_dict = {}

        # 基础信息处理
        title = soup.find_all('div', attrs={'class': 'title'})[-1].get_text()
        info = soup.find('div', attrs={'class': 'info'})
        up_date = re.search(r'\d{4}-\d{2}-\d{2}', info.get_text()).group(0)
        # 统计次数Js文件
        views_url = 'http://www.xinguizhou.com' + info.find('script').get('src')
        views = int(re.search(r'\d+', requests.get(views_url).text).group(0))

        # 所有的内容嵌套于content中的table下
        pre_content = soup.find('div', attrs = {'class': 'content'})
        content = ''
        # 段落p标签的部分
        # 对于其中出现以http://www.xinguizhou.com的链接进行处理
        for p in pre_content.find_all('p'):
            a_li = p.find_all('a')
            for a in a_li:
                if a.get('href').startswith('http://xinguizhou.com'):
                    content += '<p>' + p.get_text() + '</p>'
                else:
                    content += str(p)
            if len(a_li) <= 0:
                content += str(p)


        # 字符串空白查找替换必需移到附件表格处理之前
        content = content.strip().replace('&nbsp;', '').replace('　', '').replace(' ', '')

        # 处理信息表格
        # cellspacing="0" cellpadding="0" border="1"
        tables = pre_content.find('table').find_all('table', attrs={'cellspacing': '0', 'cellpadding': 0, 'border': '1'})
        for table in tables:
            content += str(table)
            content += '<br /><br />'

        # 处理附件表格
        # width: 450
        tables = pre_content.find('table').find_all('table', attrs={'width': '450'})
        for table in tables:
            content += '<div class="panel panel-success"><div class="panel-heading">附件下载栏</div><div class="list-group">'
            for tr in table.find_all('tr'):
                a = tr.find_all('a')[-1]
                href = a.get('href')
                if not href.startswith('http'):
                    href = 'http://www.xinguizhou.com' + href
                content += '<a target="_blank" href=" ' + href + ' " class="list-group-item">' + a.get_text() + '</a>'
            content += '</div></div></div>'

        rtn_dict['content'] = content
        rtn_dict['up_date'] = up_date
        rtn_dict['title'] = title
        rtn_dict['views'] = views
        return rtn_dict

    # 
    def getSoup(self, request):
        if request:
            try:
                return BeautifulSoup(request.text, 'html.parser')
            except Exception, e:
                print str(e)
        else:
            pass

    # 
    def getRequest(self, link = None):
        # 仅在给link赋值时request
        if link:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
                    'Host': 'xinguizhou.com',
                }
                request = requests.get(link, headers = headers)
                request.encoding = 'GB2312'
                return request
            except Exception, e:
                print str(e)
        else:
            pass