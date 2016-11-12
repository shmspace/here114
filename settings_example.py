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

task36 = {}
task36["url"] = "http://www.dianping.com/search/category/8/45/g147"
task36["name"] = "运动健身"
task36["url_base"] = "http://www.dianping.com/search/category/"
task36["url_cat"] = "8/45/"
task36["url_sub_cat"] = "g147"
task36["url_sub_cats"] = ["g147", "g151", "g2838", "g27852", "g149", "g152", "g156", "g150", "g6701", "g146"
                          , "g155", "g154", "g6702", "g153", "g6712", "g6706", "g6708", "g6709", "g6710"
                          , "g6713", "g145"]
task36["url_price"] = [0, 50, 120, 300]
task36["item_attr"] = [1,1,1,0]
task36["page"] = ""
task_list.append(task36)

task37 = {}
task37["url"] = "http://www.dianping.com/search/category/8/35/g33831"
task37["name"] = "周边游"
task37["url_base"] = "http://www.dianping.com/search/category/"
task37["url_cat"] = "8/35/"
task37["url_sub_cat"] = "g33831"
task37["url_sub_cats"] = ["g33831", "g2916", "g2926", "g2834", "g5672", "g27852", "g20038", "g22832"]
task37["url_price"] = [0, 50, 120, 300]
task37["item_attr"] = [1,1,1,0]
task37["page"] = ""
task_list.append(task37)

task38 = {}
task38["url"] = "http://www.dianping.com/search/category/8/95/g25147"
task38["name"] = "宠物"
task38["url_base"] = "http://www.dianping.com/search/category/"
task38["url_cat"] = "8/95/"
task38["url_sub_cat"] = "g25147"
task38["url_sub_cats"] = ["g25147", "g25148"]
task38["url_price"] = [0, 50, 120, 300]
task38["item_attr"] = [1,1,1,0]
task38["page"] = ""
task_list.append(task38)

# 此处之前每个需要抓取无价格分割的

task39 = {}
task39["url"] = "http://www.dianping.com/search/category/8/80/g4607"
task39["name"] = "生活服务"
task39["url_base"] = "http://www.dianping.com/search/category/"
task39["url_cat"] = "8/80/"
task39["url_sub_cat"] = "g4607"
task39["url_sub_cats"] = ["g4607", "g3064", "g3066","g33762", "g2929", "g195", "g26117", "g2976", "g2978", "g2979", 
                          "g181", "g612", "g2934", "g32742", "g2974", "g2980", "g2928", "g2932", "g836", "g197",
                          "g237", "g835", "g2930", "g979", "g980", "g25462", "g6823", "g3063", "g26465",
                          "g2884", "g3082", "g26119", "g26466", "g26491"]
task39["url_price"] = [0, 50, 120, 300]
task39["item_attr"] = [1,1,1,0]
task39["page"] = ""
task_list.append(task39)

task40 = {}
task40["url"] = "http://www.dianping.com/search/category/8/65/g2828"
task40["name"] = "爱车"
task40["url_base"] = "http://www.dianping.com/search/category/"
task40["url_cat"] = "8/65/"
task40["url_sub_cat"] = "g2828"
task40["url_sub_cats"] = ["g2828", "g176", "g178", "g20026", "g236", "g180", "g177", "g175", "g259", "g33764"]
task40["url_price"] = [0, 50, 120, 300]
task40["item_attr"] = [1,1,1,0]
task40["page"] = ""
task_list.append(task40)

task41 = {}
task41["url"] = "http://www.dianping.com/search/category/8/85/g181"
task41["name"] = "医疗健康"
task41["url_base"] = "http://www.dianping.com/search/category/"
task41["url_cat"] = "8/85/"
task41["url_sub_cat"] = "g181"
task41["url_sub_cats"] = ["g2914", "g612", "g183", "g25148", "g257", "g2912"]
task41["url_price"] = [0, 50, 120, 300]
task41["item_attr"] = [1,1,1,0]
task41["page"] = ""
task_list.append(task41)

task42 = {}
task42["url"] = "http://www.dianping.com/search/category/8/10/g112"
task42["name"] = "美食-小吃"
task42["url_base"] = "http://www.dianping.com/search/category/"
task42["url_cat"] = "8/10/"
task42["url_sub_cat"] = "g112"
task42["url_sub_cats"] = ["g112", "g210", "g219", "g1817", "g1819", "g1821", "g1827", "g1881", "g2991",
                          "g2993", "g2997", "g2999", "g3011", "g4317", "g4557", "g27835", "g32716",
                          "g32717", "g32718"]
task42["url_price"] = [0, 50, 120, 300]
task42["item_attr"] = [1,1,1,0]
task42["page"] = ""
task_list.append(task42)

task43 = {}
task43["url"] = "http://www.dianping.com/search/category/8/10/g110"
task43["name"] = "美食-火锅-川菜"
task43["url_base"] = "http://www.dianping.com/search/category/"
task43["url_cat"] = "8/10/"
task43["url_sub_cat"] = "g110"
task43["url_sub_cats"] = ["g3027", "g4273", "g4345", "g32712", "g32713", "g102",
                          "g3031", "g4467", "g4473"]
task43["url_price"] = [0, 50, 120, 300]
task43["item_attr"] = [1,1,1,0]
task43["page"] = ""
task_list.append(task43)

task44 = {}
task44["url"] = "http://www.dianping.com/search/category/8/10/g111"
task44["name"] = "美食-自助餐-咖啡厅-日本料理-西餐-烧烤-串串香-茶馆"
task44["url_base"] = "http://www.dianping.com/search/category/"
task44["url_cat"] = "8/10/"
task44["url_sub_cat"] = "g111"
task44["url_sub_cats"] = ["g111", "g132", "g224", "g116", "g508", "g3017", "g134"]
task44["url_price"] = [0, 50, 120, 300]
task44["item_attr"] = [1,1,1,0]
task44["page"] = ""
task_list.append(task44)

task45 = {}
task45["url"] = "http://www.dianping.com/search/category/8/10/g117"
task45["name"] = "美食-面包甜点-韩国料理-东南亚菜-海鲜-私房菜-粤菜-清真菜-新疆菜"
task45["url_base"] = "http://www.dianping.com/search/category/"
task45["url_cat"] = "8/10/"
task45["url_sub_cat"] = "g117"
task45["url_sub_cats"] = ["g108", "g3243"]
task45["url_price"] = [0, 50, 120, 300]
task45["item_attr"] = [1,1,1,0]
task45["page"] = ""
task_list.append(task45)

task46 = {}
task46["url"] = "http://www.dianping.com/search/category/8/10/g118"
task46["name"] = "美食-其它"
task46["url_base"] = "http://www.dianping.com/search/category/"
task46["url_cat"] = "8/10/"
task46["url_sub_cat"] = "g118"
task46["url_sub_cats"] = ["g118", "g133", "g101", "g104", "g106", "g109", "g247", "g252", "g311",
                          "g1871", "g6743", "g26481", "g26482", "g26483"]
task46["url_price"] = [0, 50, 120, 300]
task46["item_attr"] = [1,1,1,0]
task46["page"] = ""
task_list.append(task46)

task47 = {}
task47["url"] = "http://www.dianping.com/search/category/8/30/g135"
task47["name"] = "休闲娱乐-KTV-足疗按摩-咖啡厅-酒吧-洗浴-轰趴馆-茶馆"
task47["url_base"] = "http://www.dianping.com/search/category/"
task47["url_cat"] = "8/30/"
task47["url_sub_cat"] = "g135"
task47["url_sub_cats"] = ["g135", "g141", "g132", "g133", "g140", "g20040", "g134", "g134r39", "g134r35",
                          "g134r37", "g134c1604", "g134r36", "g134r38", "g134c1605", "g134r4956", "g134r27623",
                          "g134r27622", "g134r27619", "g134c1608", "g134c1609", "g134c1610", "g134c1611",
                          "g134c1612", "g134c1613", "g134c4425", "g134c4424"]
task47["url_price"] = [0, 50, 120, 300]
task47["item_attr"] = [1,1,1,0]
task47["page"] = ""
task_list.append(task47)

task48 = {}
task48["url"] = "http://www.dianping.com/search/category/8/50/g157"
task48["name"] = "丽人-美发"
task48["url_base"] = "http://www.dianping.com/search/category/"
task48["url_cat"] = "8/50/"
task48["url_sub_cat"] = "g157"
task48["url_sub_cats"] = ["g157", "g157r39", "g157r35", "g157r37", "g157c1604", "g157r36", "g157r38", "g157c1605",
                          "g157r4956", "g157r27623", "g157r27622", "g157r27619", "g157c1608", "g157c1609",
                          "g157c1610", "g157c1611", "g157c1612", "g157c1613", "g157c4425", "g157c4424"]
task48["url_price"] = [0, 50, 120, 300]
task48["item_attr"] = [1,1,1,0]
task48["page"] = ""
task_list.append(task48)

task49 = {}
task49["url"] = "http://www.dianping.com/search/category/8/50/g158"
task49["name"] = "丽人-spa-美甲"
task49["url_base"] = "http://www.dianping.com/search/category/"
task49["url_cat"] = "8/50/"
task49["url_sub_cat"] = "g158"
task49["url_sub_cats"] = ["g158", "g158r39", "g158r35", "g158r37", "g158c1604", "g158r36", "g158r38", "g158c1605",
                          "g158r4956", "g158r27623", "g158r27622", "g158r27619", "g158c1608", "g158c1609",
                          "g158c1610", "g158c1611", "g158c1612", "g158c1613", "g158c4425", "g158c4424", "g33761"]
task49["url_price"] = [0, 50, 120, 300]
task49["item_attr"] = [1,1,1,0]
task49["page"] = ""
task_list.append(task49)

task50 = {}
task50["url"] = "http://www.dianping.com/search/category/8/50/g148"
task50["name"] = "丽人-瑜伽-舞蹈-纹绣-瘦身-纹身-化妆品-祛痘-整形-产后塑形"
task50["url_base"] = "http://www.dianping.com/search/category/"
task50["url_cat"] = "8/50/"
task50["url_sub_cat"] = "g148"
task50["url_sub_cats"] = ["g148", "g149", "g2898", "g159", "g493", "g123", "g2572", "g183", "g2790"]
task50["url_price"] = [0, 50, 120, 300]
task50["item_attr"] = [1,1,1,0]
task50["page"] = ""
task_list.append(task50)

task51 = {}
task51["url"] = "http://www.dianping.com/search/category/8/45/g147"
task51["name"] = "运动健身-健身中心-游泳馆-瑜伽-舞蹈-羽毛球-台球馆"
task51["url_base"] = "http://www.dianping.com/search/category/"
task51["url_cat"] = "8/45/"
task51["url_sub_cat"] = "g147"
task51["url_sub_cats"] = ["g147", "g151", "g148", "g149", "g152", "g156"]
task51["url_price"] = [0, 50, 120, 300]
task51["item_attr"] = [1,1,1,0]
task51["page"] = ""
task_list.append(task51)

task52 = {}
task52["url"] = "http://www.dianping.com/search/category/8/35/g33831"
task52["name"] = "周边游-景点"
task52["url_base"] = "http://www.dianping.com/search/category/"
task52["url_cat"] = "8/35/"
task52["url_sub_cat"] = "g33831"
task52["url_sub_cats"] = ["g33831", "g2926", "g2916", "g2834", "g5672", "g20038"]
task52["url_price"] = [0, 50, 120, 300]
task52["item_attr"] = [1,1,1,0]
task52["page"] = ""
task_list.append(task52)

task53 = {}
task53["url"] = "http://www.dianping.com/search/category/8/39/g25147"
task53["name"] = "宠物"
task53["url_base"] = "http://www.dianping.com/search/category/"
task53["url_cat"] = "8/95/"
task53["url_sub_cat"] = "g25147"
task53["url_sub_cats"] = ["g25147", "g25148"]
task53["url_price"] = [0, 50, 120, 300]
task53["item_attr"] = [1,1,1,0]
task53["page"] = ""
task_list.append(task53)

task54 = {}
task54["url"] = "http://www.dianping.com/search/category/8/75/g2872"
task54["name"] = "学习培训"
task54["url_base"] = "http://www.dianping.com/search/category/"
task54["url_cat"] = "8/75/"
task54["url_sub_cat"] = "g2872"
task54["url_sub_cats"] = ["g2872", "g2873", "g2877", "g2876", "g2874", "g2878", "g179", "g260", "g189",
                          "g190", "g2906", "g2908", "g2910", "g32748", "g2882", "g32722"]
task54["url_price"] = [0, 50, 120, 300]
task54["item_attr"] = [1,1,1,0]
task54["page"] = ""
task_list.append(task54)

####### 绵阳 ########
task55 = {}
task55["url"] = "http://www.dianping.com/search/category/242/10/g110"
task55["name"] = "[绵阳]美食"
task55["url_base"] = "http://www.dianping.com/search/category/"
task55["url_cat"] = "242/10/"
task55["url_sub_cat"] = "g110"
task55["url_sub_cats"] = ["g110", "g117", "g111", "g102", "g116", "g132", "g508", "g113", "g114",
                          "g133", "g134", "g217", "g103", "g210", "g118"]
task55["url_price"] = [0, 50, 120, 300]
task55["item_attr"] = [1,1,1,0]
task55["page"] = ""
task_list.append(task55)

task56 = {}
task56["url"] = "http://www.dianping.com/search/category/242/30"
task56["name"] = "[绵阳]休闲娱乐"
task56["url_base"] = "http://www.dianping.com/search/category/"
task56["url_cat"] = "242/30/"
task56["url_sub_cat"] = ""
task56["url_sub_cats"] = [""]
task56["url_price"] = [0, 50, 120, 300]
task56["item_attr"] = [1,1,1,0]
task56["page"] = ""
task_list.append(task56)

task57 = {}
task57["url"] = "http://www.dianping.com/search/category/242/50"
task57["name"] = "[绵阳]丽人"
task57["url_base"] = "http://www.dianping.com/search/category/"
task57["url_cat"] = "242/50/"
task57["url_sub_cat"] = ""
task57["url_sub_cats"] = [""]
task57["url_price"] = [0, 50, 120, 300]
task57["item_attr"] = [1,1,1,0]
task57["page"] = ""
task_list.append(task57)

task58 = {}
task58["url"] = "http://www.dianping.com/search/category/242/80"
task58["name"] = "[绵阳]生活服务"
task58["url_base"] = "http://www.dianping.com/search/category/"
task58["url_cat"] = "242/80/"
task58["url_sub_cat"] = ""
task58["url_sub_cats"] = [""]
task58["url_price"] = [0, 50, 120, 300]
task58["item_attr"] = [1,1,1,0]
task58["page"] = ""
task_list.append(task58)

task59 = {}
task59["url"] = "http://www.dianping.com/search/category/242/65"
task59["name"] = "[绵阳]爱车服务"
task59["url_base"] = "http://www.dianping.com/search/category/"
task59["url_cat"] = "242/65/"
task59["url_sub_cat"] = ""
task59["url_sub_cats"] = [""]
task59["url_price"] = [0, 50, 120, 300]
task59["item_attr"] = [1,1,1,0]
task59["page"] = ""
task_list.append(task59)

task60 = {}
task60["url"] = "http://www.dianping.com/search/category/242/85"
task60["name"] = "[绵阳]医疗健康"
task60["url_base"] = "http://www.dianping.com/search/category/"
task60["url_cat"] = "242/85/"
task60["url_sub_cat"] = ""
task60["url_sub_cats"] = [""]
task60["url_price"] = [0, 50, 120, 300]
task60["item_attr"] = [1,1,1,0]
task60["page"] = ""
task_list.append(task60)



















task_for_crawler = {}
#task_for_crawler["crawler01"] = [task_list[51], task_list[52], task_list[38]]
#task_for_crawler["crawler02"] = [task_list[46]]
#task_for_crawler["crawler03"] = [task_list[55], task_list[56], task_list[57], task_list[58],
#                                 task_list[59], task_list[60]]
#task_for_crawler["crawler04"] = [task_list[48]]
task_for_crawler["crawler04"] = [task_list[55], task_list[56], task_list[57], task_list[58],
                                 task_list[59], task_list[60]]

