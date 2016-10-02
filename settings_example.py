#!/usr/bin/env python
#coding:utf-8

# vnc启动
# cp /lib/systemd/system/vncserver@.service /lib/systemd/system/vncserver@:2.service
# vim /lib/systemd/system/vncserver@:2.service
# systemctl stop firewalld.service
# systemctl disable firewalld.service
# systemctl daemon-reload
# vncpasswd root
# systemctl start vncserver@:2.service
# systemctl enable vncserver@:2.service

# 服务器地址
#server_url = "http://123.207.1.180:8080"
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

task2 = {}
task2["url"] = "http://www.dianping.com/search/category/8/10/g110x39y40"
task2["name"] = "美食-火锅"
task2["url_base"] = "http://www.dianping.com/search/category/"
task2["url_cat"] = "8/10/"
task2["url_sub_cat"] = "g110"
task2["url_price"] = [180, 180, 260]
task2["item_attr"] = [1,1,1,0]
task2["page"] = ""
task_list.append(task2)

task3 = {}
task3["url"] = "http://www.dianping.com/search/category/8/10/g112x39y40"
task3["name"] = "美食-小吃快餐"
task3["url_base"] = "http://www.dianping.com/search/category/"
task3["url_cat"] = "8/10/"
task3["url_sub_cat"] = "g112"
task3["url_price"] = [18, 18, 28, 38, 48, 68, 100, 120]
task3["item_attr"] = [1,1,1,0]
task3["page"] = "p29"
task_list.append(task3)

task4 = {}
task4["url"] = "http://www.dianping.com/search/category/8/10/g112x39y40"
task4["name"] = "美食-小吃快餐"
task4["url_base"] = "http://www.dianping.com/search/category/"
task4["url_cat"] = "8/10/"
task4["url_sub_cat"] = "g102"
task4["url_price"] = [42, 50, 60, 80, 120, 300]
task4["item_attr"] = [1,1,1,0]
task4["page"] = "p32"
task_list.append(task4)

task5 = {}
task5["url"] = "http://www.dianping.com/search/category/8/10/g111"
task5["name"] = "美食-自助餐"
task5["url_base"] = "http://www.dianping.com/search/category/"
task5["url_cat"] = "8/10/"
task5["url_sub_cat"] = "g111"
task5["url_price"] = [0, 50, 120, 300]
task5["item_attr"] = [1,1,1,0]
task5["page"] = ""
task_list.append(task5)

task6 = {}
task6["url"] = "http://www.dianping.com/search/category/8/10/g132"
task6["name"] = "美食-咖啡厅"
task6["url_base"] = "http://www.dianping.com/search/category/"
task6["url_cat"] = "8/10/"
task6["url_sub_cat"] = "g132"
task6["url_price"] = [0, 50, 120, 300]
task6["item_attr"] = [1,1,1,0]
task6["page"] = ""
task_list.append(task6)

task7 = {}
task7["url"] = "http://www.dianping.com/search/category/8/10/g224"
task7["name"] = "美食-日本料理"
task7["url_base"] = "http://www.dianping.com/search/category/"
task7["url_cat"] = "8/10/"
task7["url_sub_cat"] = "g224"
task7["url_price"] = [0, 50, 120, 300]
task7["item_attr"] = [1,1,1,0]
task7["page"] = ""
task_list.append(task7)

task8 = {}
task8["url"] = "http://www.dianping.com/search/category/8/10/g116"
task8["name"] = "美食-西餐"
task8["url_base"] = "http://www.dianping.com/search/category/"
task8["url_cat"] = "8/10/"
task8["url_sub_cat"] = "g116"
task8["url_price"] = [0, 50, 120, 300]
task8["item_attr"] = [1,1,1,0]
task8["page"] = ""
task_list.append(task8)

task9 = {}
task9["url"] = "http://www.dianping.com/search/category/8/10/g508"
task9["name"] = "美食-烧烤"
task9["url_base"] = "http://www.dianping.com/search/category/"
task9["url_cat"] = "8/10/"
task9["url_sub_cat"] = "g508"
task9["url_price"] = [0, 50, 120, 300]
task9["item_attr"] = [1,1,1,0]
task9["page"] = ""
task_list.append(task9)





task_for_crawler = {}
task_for_crawler["crawler01"] = [task_list[7]]
task_for_crawler["crawler02"] = [task_list[8]]

