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

print settings.dianping_url_map

def save_it_to_server(page_url, item_url, tasks_id, page, crawler):
    data = {}
    data["tasks_id"] = tasks_id
    data["url"] = item_url
    data["page_url"] = page_url
    data["page"] = page
    data["crawler"] = crawler
    url = "http://localhost:8882/index.php?r=api/site/addit"
    req = urllib2.urlopen(url, post_data)
    return req.read()

dianping_pager = page.Pager()
result = dianping_pager.list_page_links(settings.dianping_url_map['waiyu'])
print result["next_page"]

for item in result["items"]:
    save_it_to_server(page_url, item_url, tasks_id, page, crawler)






