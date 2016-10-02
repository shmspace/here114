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
crawler = "crawler04"

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

task10 = {}
task10["url"] = "http://www.dianping.com/search/category/8/10/g3017"
task10["name"] = "美食-串串香"
task10["url_base"] = "http://www.dianping.com/search/category/"
task10["url_cat"] = "8/10/"
task10["url_sub_cat"] = "g3017"
task10["url_price"] = [0, 50, 120, 300]
task10["item_attr"] = [1,1,1,0]
task10["page"] = ""
task_list.append(task10)

task11 = {}
task11["url"] = "http://www.dianping.com/search/category/8/10/g134"
task11["name"] = "美食-茶馆"
task11["url_base"] = "http://www.dianping.com/search/category/"
task11["url_cat"] = "8/10/"
task11["url_sub_cat"] = "g134"
task11["url_price"] = [0, 50, 120, 300]
task11["item_attr"] = [1,1,1,0]
task11["page"] = ""
task_list.append(task11)

task12 = {}
task12["url"] = "http://www.dianping.com/search/category/8/10/g117"
task12["name"] = "美食-面包甜点"
task12["url_base"] = "http://www.dianping.com/search/category/"
task12["url_cat"] = "8/10/"
task12["url_sub_cat"] = "g117"
task12["url_price"] = [12, 14, 50, 120, 300]
task12["item_attr"] = [1,1,1,0]
task12["page"] = "p29"
task_list.append(task12)

task13 = {}
task13["url"] = "http://www.dianping.com/search/category/8/10/g114"
task13["name"] = "美食-韩国料理"
task13["url_base"] = "http://www.dianping.com/search/category/"
task13["url_cat"] = "8/10/"
task13["url_sub_cat"] = "g114"
task13["url_price"] = [0, 50, 120, 300]
task13["item_attr"] = [1,1,1,0]
task13["page"] = ""
task_list.append(task13)

task14 = {}
task14["url"] = "http://www.dianping.com/search/category/8/10/g115"
task14["name"] = "美食-东南亚菜"
task14["url_base"] = "http://www.dianping.com/search/category/"
task14["url_cat"] = "8/10/"
task14["url_sub_cat"] = "g115"
task14["url_price"] = [0, 50, 120, 300]
task14["item_attr"] = [1,1,1,0]
task14["page"] = ""
task_list.append(task14)

task15 = {}
task15["url"] = "http://www.dianping.com/search/category/8/10/g251"
task15["name"] = "美食-海鲜"
task15["url_base"] = "http://www.dianping.com/search/category/"
task15["url_cat"] = "8/10/"
task15["url_sub_cat"] = "g251"
task15["url_price"] = [0, 50, 120, 300]
task15["item_attr"] = [1,1,1,0]
task15["page"] = ""
task_list.append(task15)

task16 = {}
task16["url"] = "http://www.dianping.com/search/category/8/10/g1338"
task16["name"] = "美食-私房菜"
task16["url_base"] = "http://www.dianping.com/search/category/"
task16["url_cat"] = "8/10/"
task16["url_sub_cat"] = "g1338"
task16["url_price"] = [0, 50, 120, 300]
task16["item_attr"] = [1,1,1,0]
task16["page"] = ""
task_list.append(task16)

task17 = {}
task17["url"] = "http://www.dianping.com/search/category/8/10/g103"
task17["name"] = "美食-粤菜"
task17["url_base"] = "http://www.dianping.com/search/category/"
task17["url_cat"] = "8/10/"
task17["url_sub_cat"] = "g103"
task17["url_price"] = [0, 50, 120, 300]
task17["item_attr"] = [1,1,1,0]
task17["page"] = ""
task_list.append(task17)

task18 = {}
task18["url"] = "http://www.dianping.com/search/category/8/10/g108"
task18["name"] = "美食-清真菜"
task18["url_base"] = "http://www.dianping.com/search/category/"
task18["url_cat"] = "8/10/"
task18["url_sub_cat"] = "g108"
task18["url_price"] = [0, 50, 120, 300]
task18["item_attr"] = [1,1,1,0]
task18["page"] = ""
task_list.append(task18)

task19 = {}
task19["url"] = "http://www.dianping.com/search/category/8/10/g3243"
task19["name"] = "美食-新疆菜"
task19["url_base"] = "http://www.dianping.com/search/category/"
task19["url_cat"] = "8/10/"
task19["url_sub_cat"] = "g3243"
task19["url_price"] = [0, 50, 120, 300]
task19["item_attr"] = [1,1,1,0]
task19["page"] = ""
task_list.append(task19)

task20 = {}
task20["url"] = "http://www.dianping.com/search/category/8/10/g118"
task20["name"] = "美食-其它"
task20["url_base"] = "http://www.dianping.com/search/category/"
task20["url_cat"] = "8/10/"
task20["url_sub_cat"] = "g118"
task20["url_price"] = [25, 37, 50, 120, 300]
task20["item_attr"] = [1,1,1,0]
task20["page"] = "p14"
task_list.append(task20)

task21 = {}
task21["url"] = "http://www.dianping.com/search/category/8/10/g136"
task21["name"] = "电影院"
task21["url_base"] = "http://www.dianping.com/search/category/"
task21["url_cat"] = "8/10/"
task21["url_sub_cat"] = "g136"
task21["url_price"] = [0, 50, 120, 300]
task21["item_attr"] = [1,1,1,0]
task21["page"] = ""
task_list.append(task21)

task22 = {}
task22["url"] = "http://www.dianping.com/search/category/8/10/g135"
task22["name"] = "休闲娱乐-ktv"
task22["url_base"] = "http://www.dianping.com/search/category/"
task22["url_cat"] = "8/10/"
task22["url_sub_cat"] = "g135"
task22["url_price"] = [0, 50, 120, 300]
task22["item_attr"] = [1,1,1,0]
task22["page"] = ""
task_list.append(task22)

task23 = {}
task23["url"] = "http://www.dianping.com/search/category/8/10/g141"
task23["name"] = "休闲娱乐-足疗按摩"
task23["url_base"] = "http://www.dianping.com/search/category/"
task23["url_cat"] = "8/10/"
task23["url_sub_cat"] = "g141"
task23["url_price"] = [50, 120, 300]
task23["item_attr"] = [1,1,1,0]
task23["page"] = "p19"
task_list.append(task23)

task24 = {}
task24["url"] = "http://www.dianping.com/search/category/8/10/g132"
task24["name"] = "休闲娱乐-咖啡厅"
task24["url_base"] = "http://www.dianping.com/search/category/"
task24["url_cat"] = "8/10/"
task24["url_sub_cat"] = "g132"
task24["url_price"] = [0, 50, 120, 300]
task24["item_attr"] = [1,1,1,0]
task24["page"] = ""
task_list.append(task24)

task25 = {}
task25["url"] = "http://www.dianping.com/search/category/8/10/g133"
task25["name"] = "休闲娱乐-酒吧"
task25["url_base"] = "http://www.dianping.com/search/category/"
task25["url_cat"] = "8/10/"
task25["url_sub_cat"] = "g133"
task25["url_price"] = [0, 50, 120, 300]
task25["item_attr"] = [1,1,1,0]
task25["page"] = ""
task_list.append(task25)

task26 = {}
task26["url"] = "http://www.dianping.com/search/category/8/10/g140"
task26["name"] = "休闲娱乐-洗浴"
task26["url_base"] = "http://www.dianping.com/search/category/"
task26["url_cat"] = "8/10/"
task26["url_sub_cat"] = "g140"
task26["url_price"] = [0, 50, 120, 300]
task26["item_attr"] = [1,1,1,0]
task26["page"] = ""
task_list.append(task26)

task27 = {}
task27["url"] = "http://www.dianping.com/search/category/8/10/g20040"
task27["name"] = "休闲娱乐-轰趴馆"
task27["url_base"] = "http://www.dianping.com/search/category/"
task27["url_cat"] = "8/10/"
task27["url_sub_cat"] = "g20040"
task27["url_price"] = [0, 50, 120, 300]
task27["item_attr"] = [1,1,1,0]
task27["page"] = ""
task_list.append(task27)

task28 = {}
task28["url"] = "http://www.dianping.com/search/category/8/10/g20042"
task28["name"] = "休闲娱乐-网吧网咖"
task28["url_base"] = "http://www.dianping.com/search/category/"
task28["url_cat"] = "8/10/"
task28["url_sub_cat"] = "g20042"
task28["url_price"] = [0, 50, 120, 300]
task28["item_attr"] = [1,1,1,0]
task28["page"] = ""
task_list.append(task28)

task29 = {}
task29["url"] = "http://www.dianping.com/search/category/8/10/g144"
task29["name"] = "休闲娱乐-DIY手工坊"
task29["url_base"] = "http://www.dianping.com/search/category/"
task29["url_cat"] = "8/10/"
task29["url_sub_cat"] = "g144"
task29["url_price"] = [0, 50, 120, 300]
task29["item_attr"] = [1,1,1,0]
task29["page"] = ""
task_list.append(task29)

task30 = {}
task30["url"] = "http://www.dianping.com/search/category/8/10/g2754"
task30["name"] = "休闲娱乐-密室"
task30["url_base"] = "http://www.dianping.com/search/category/"
task30["url_cat"] = "8/10/"
task30["url_sub_cat"] = "g2754"
task30["url_price"] = [0, 50, 120, 300]
task30["item_attr"] = [1,1,1,0]
task30["page"] = ""
task_list.append(task30)

task31 = {}
task31["url"] = "http://www.dianping.com/search/category/8/10/g20039"
task31["name"] = "休闲娱乐-真人cs"
task31["url_base"] = "http://www.dianping.com/search/category/"
task31["url_cat"] = "8/10/"
task31["url_sub_cat"] = "g20039"
task31["url_price"] = [0, 50, 120, 300]
task31["item_attr"] = [1,1,1,0]
task31["page"] = ""
task_list.append(task31)

task32 = {}
task32["url"] = "http://www.dianping.com/search/category/8/10/g137"
task32["name"] = "休闲娱乐-游乐游艺"
task32["url_base"] = "http://www.dianping.com/search/category/"
task32["url_cat"] = "8/10/"
task32["url_sub_cat"] = "g137"
task32["url_price"] = [0, 50, 120, 300]
task32["item_attr"] = [1,1,1,0]
task32["page"] = ""
task_list.append(task32)

task33 = {}
task33["url"] = "http://www.dianping.com/search/category/8/10/g20038"
task33["name"] = "休闲娱乐-农家乐"
task33["url_base"] = "http://www.dianping.com/search/category/"
task33["url_cat"] = "8/10/"
task33["url_sub_cat"] = "g20038"
task33["url_price"] = [0, 50, 120, 300]
task33["item_attr"] = [1,1,1,0]
task33["page"] = ""
task_list.append(task33)

task34 = {}
task34["url"] = "http://www.dianping.com/search/category/8/10/g156"
task34["name"] = "休闲娱乐-台球馆"
task34["url_base"] = "http://www.dianping.com/search/category/"
task34["url_cat"] = "8/10/"
task34["url_sub_cat"] = "g156"
task34["url_price"] = [0, 50, 120, 300]
task34["item_attr"] = [1,1,1,0]
task34["page"] = ""
task_list.append(task34)

task35 = {}
task35["url"] = "http://www.dianping.com/search/category/8/10/g157"
task35["name"] = "休闲娱乐-丽人"
task35["url_base"] = "http://www.dianping.com/search/category/"
task35["url_cat"] = "8/50/"
task35["url_sub_cat"] = "g157"
task35["url_sub_cats"] = ["g157", "g158", "g33761", "g148", "g149", "g2898", "g159", "g493", "g123", "g2572"
                          , "g183", "g2790"]
task35["url_price"] = [0, 50, 120, 300]
task35["item_attr"] = [1,1,1,0]
task35["page"] = ""
task_list.append(task35)



















task_for_crawler = {}
task_for_crawler["crawler01"] = [task_list[34]]
task_for_crawler["crawler02"] = [task_list[11], task_list[12], task_list[13], task_list[14]]
task_for_crawler["crawler03"] = [task_list[19]]
task_for_crawler["crawler04"] = [task_list[22], task_list[23], task_list[24], task_list[25], task_list[26]]

