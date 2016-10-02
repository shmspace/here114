#!/usr/bin/env python
#coding:utf-8

import settings
import page_selenium as page
import types
import xlrd
import xlwt as ExcelWrite
import time
import urllib2
import urllib
import json


url_list = []

page_info = settings.task3

dianping_pager = page.Pager()
#dianping_pager.init_category(page_info)
#category_url = dianping_pager.check_category_url()
#dianping_pager.check_next_category_url()
#dianping_pager.check_next_category_url()
#dianping_pager.check_next_category_url()

#result = dianping_pager.list_page_links(category_url)
#print result
#url = u"http://www.dianping.com/shop/22998876"
url = u"http://www.dianping.com/shop/5426914"
item_info = dianping_pager.get_item_info(url, page_info["item_attr"])
dianping_pager.close()
