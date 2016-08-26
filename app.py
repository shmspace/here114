#!/usr/bin/env python
#coding:utf-8

import settings
import page

print settings.dianping_url_map

def print_item_info(item_info):
    print "title:      %s"% item_info["title"]
    print "phone:      %s"% item_info["phone"]
    print "address:    %s"% item_info["address"]
    print "description %s"% item_info["description"]

shop_info = []

dianping_pager = page.Pager()
result = dianping_pager.list_page_links(settings.dianping_url_map['waiyu'])
print result["next_page"]

for item in result["items"]:
    item_info = dianping_pager.get_item_info(item)
    shop_info.append(item_info)
    print_item_info(item_info)

while result["next_page"] != "":
    dianping_pager = page.Pager()
    result = dianping_pager.list_page_links(result["next_page"])
    for item in result["items"]:
        item_info = dianping_pager.get_item_info(item)
        shop_info.append(item_info)
        print_item_info(item_info)

