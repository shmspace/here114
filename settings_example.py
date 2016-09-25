#!/usr/bin/env python
#coding:utf-8

# 服务器地址
server_url = "http://localhost:8882"

# 机器名称
crawler = "crawler01"

# 本地保存excel文件地址
is_save_file = False
output_xls_file = "/Users/yaoyilin/dev/python/here114/doc/item_info_waiyu.xls"

# 点评分类列表
dianping_url_map = {}
# dianping_url_map['jiaoyu'] = "http://www.dianping.com/search/category/1/75/g2872"
dianping_url_map['jiaoyu'] = "http://www.dianping.com/search/category/8/75"
dianping_url_map['waiyu'] = "http://www.dianping.com/search/category/8/75/g2872"

task_list = []
task = {}

task["url"] = "http://www.dianping.com/search/category/8/75/m3"
task["name"] = "学习培训-有团购"
task["max_page"] = 13
task["title_xpath"] = u"//div[@class='brief-info']/div[@class='address']|//div[@class='shop-info']/div[@class='shop-addr']/span|//div[@itemprop='street-address']"
task["address_xpath"] = u"//div[@class='brief-info']/div[@class='address']|//div[@class='shop-info']/div[@class='shop-addr']/span|//div[@itemprop='street-address']"
task["phone_xpath"] = u"//div[@class='book']/div[@class='phone']/span|//div[@class='shop-info']/div[@class='shopinfor']/p/span[1]|//span[@itemprop='tel']"
task["desc_xpath"] = u"//div[@class='mod-wrap']/div[@id='info']/ul/li[2]|//div[@class='con J_showWarp']/div[@class='block_all']/div[2]/span"
task_list.append(task)

task_for_crawler = {}
task_for_crawler["crawler01"] = [task_list[0]]

