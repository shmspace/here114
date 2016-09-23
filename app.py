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

def print_item_info(item_info):
    print "title:      %s"% item_info["title"]
    print "phone:      %s"% item_info["phone"]
    print "address:    %s"% item_info["address"]
    print "description %s"% item_info["description"]

def save_to_server(item_info, category, item_url, list_url, crawler):
    data = {}
    data["name"] = item_info["title"]
    data["phone"] = item_info["phone"]
    data["adress"] = item_info["address"]
    data["description"] = item_info["description"]
    data["category"] = category
    data["item_url"] = item_url
    data["list_url"] = list_url
    data["crawler"] = crawler
    url = "http://localhost:8882/index.php?r=api/site"
    post_data = urllib.urlencode(data)
    req = urllib2.urlopen(url, post_data)
    return req.read()


shop_info = []

# 保存excel
output_xls_file = "/Users/yaoyilin/dev/python/here114/doc/item_info_waiyu.xls"
xls = ExcelWrite.Workbook()
sheet = xls.add_sheet("Sheet1")
i = 0

dianping_pager = page.Pager()
result = dianping_pager.list_page_links(settings.dianping_url_map['waiyu'])
print result["next_page"]

for item in result["items"]:
    try:
        item_info = dianping_pager.get_item_info(item)
    except Exception,e:
        time.sleep(30)
        item_info = dianping_pager.get_item_info(item)
    shop_info.append(item_info)
    print_item_info(item_info)
    save_to_server(item_info, "waiyu", item, settings.dianping_url_map['waiyu'], "crawler01")

    sheet.write(i, 0, item_info["title"].decode("utf-8"))
    sheet.write(i, 1, item_info["phone"].decode("utf-8"))
    sheet.write(i, 2, item_info["address"].decode("utf-8"))
    sheet.write(i, 3, item_info["description"].decode("utf-8"))
    sheet.write(i, 4, item)
    i = i + 1
if i/15*15 == i:
    print "开始保存..."
    xls.save(output_xls_file)
    print "保存成功..."

while result["next_page"] != "":
    #dianping_pager = page.Pager()
    current_page_url = result["next_page"]
    try:
        result = dianping_pager.list_page_links(result["next_page"])
    except Exception,e:
        time.sleep(30)
        result = dianping_pager.list_page_links(result["next_page"])
    for item in result["items"]:
        try:
            item_info = dianping_pager.get_item_info(item)
        except Exception,e:
            time.sleep(30)
            item_info = dianping_pager.get_item_info(item)
        shop_info.append(item_info)
        print_item_info(item_info)
        save_to_server(item_info, "waiyu", item, current_page_url, "crawler01")

        sheet.write(i, 0, item_info["title"].decode("utf-8"))
        sheet.write(i, 1, item_info["phone"].decode("utf-8"))
        sheet.write(i, 2, item_info["address"].decode("utf-8"))
        sheet.write(i, 3, item_info["description"].decode("utf-8"))
        sheet.write(i, 4, item)
        i = i + 1
    if i/15*15 == i:
        print "开始保存..."
        xls.save(output_xls_file)
        print "保存成功..."
xls.save(output_xls_file)
