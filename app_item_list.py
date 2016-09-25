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

def save_item_to_server(item_info, category, item_url, list_url, crawler, item_tasks_id):
    data = {}
    data["name"] = item_info["title"]
    data["phone"] = item_info["phone"]
    data["adress"] = item_info["address"]
    data["description"] = item_info["description"]
    data["category"] = category
    data["item_url"] = item_url
    data["list_url"] = list_url
    data["crawler"] = crawler
    data["item_tasks_id"] = item_tasks_id
    url = "http://localhost:8882/index.php?r=api/site"
    post_data = urllib.urlencode(data)
    print post_data
    req = urllib2.urlopen(url, post_data)
    print "Item 数据发送服务器保存成功......"
    result = req.read()
    print result
    reqs = json.loads(result)
    return reqs

def save_it_to_server(page_url, item_url, tasks_id, page, crawler):
    data = {}
    data["tasks_id"] = tasks_id
    data["url"] = item_url
    data["page_url"] = page_url
    data["page"] = page
    data["crawler"] = crawler
    url = "http://localhost:8882/index.php?r=api/site/addit"
    post_data = urllib.urlencode(data)
    print post_data
    req = urllib2.urlopen(url, post_data)
    print "Item Task 数据发送服务器保存成功......"
    result = req.read()
    print result
    reqs = json.loads(result)
    return reqs

def save_shop_to_server(item_info):
    pass

page_info = settings.task_for_crawler[settings.crawler][0]
page_url = page_info["url"]
#page_url = settings.dianping_url_map['waiyu']
dianping_pager = page.Pager()
while 1:
    print page_url
    result = dianping_pager.list_page_links(page_url)
    if result["rs"] == "-1":
        print "打开页面失败，暂停抓取5分钟..."
        dianping_pager.close()
        time.sleep(1)
        dianping_pager = page.Pager()
        for i in range(1, 20):
            time.sleep(1)
            print "打开页面失败，暂停抓取5分钟...%d"%(20 - i)
        continue
    elif result["rs"] == "-2":
        print "本类目抓取完成..."
        dianping_pager.close()
        time.sleep(1)
        dianping_pager = page.Pager()
        break

    for item in result["items"]:
        rs = save_it_to_server(page_url, item, -1, result["page"], settings.crawler)
        if rs["item_status"] == 0:
            item_info = dianping_pager.get_item_info(item)
            irs = save_item_to_server(item_info, page_info["name"], item, page_url, settings.crawler, rs["items_id"])
            print irs

    if result["next_page"] != "":
        page_url = result["next_page"]
    else:
        dianping_pager.close()
        time.sleep(1)
        dianping_pager = page.Pager()




