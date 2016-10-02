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
    url = "%s/index.php?r=api/site" % settings.server_url
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
    url = "%s/index.php?r=api/site/addit" % settings.server_url
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

tasks_no = 0
page_info = settings.task_for_crawler[settings.crawler][tasks_no]
dianping_pager = page.Pager()
dianping_pager.init_category(page_info)
page_url = dianping_pager.check_category_url()

while 1:
    print page_url
    result = dianping_pager.list_page_links(page_url)
    if result["rs"] == "-1":
        print "打开页面失败，暂停抓取5分钟..."
        dianping_pager.close()
        time.sleep(1)
        dianping_pager.init_br()
        for i in range(1, 20):
            time.sleep(1)
            print "打开页面失败，暂停抓取20秒...%d"%(20 - i)
        continue

    for item in result["items"]:
        rs = save_it_to_server(page_url, item, -1, result["page"], settings.crawler)
        if rs["item_status"] == 0:
            try:
                item_info = dianping_pager.get_item_info(item, page_info["item_attr"])
            except Exception, e:
                print e
                for i in range(1, 180):
                    time.sleep(10)
                    print "打开页面失败，暂停抓取1800秒...%d"%(180 - i)
                continue
            irs = save_item_to_server(item_info, page_info["name"], item, page_url, settings.crawler, rs["items_id"])
            print irs

    if result["next_page"] != "":
        page_url = result["next_page"]
    else:
        page_url = dianping_pager.check_next_category_url()
        if page_url == -1:
            tasks_no = tasks_no + 1
            if len(settings.task_for_crawler[settings.crawler]) > tasks_no:
                page_info =  settings.task_for_crawler[settings.crawler][tasks_no]
                dianping_pager.init_category(page_info)
                page_url = dianping_pager.check_category_url()
            else:
                dianping_pager.close()
                print "crawler is ok ....."
                break
            # time.sleep(1)
            # dianping_pager.init_br()




