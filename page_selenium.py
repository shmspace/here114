#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys #引入keys类操作

import os
import time
import random
import re
import HTMLParser

ROOT_DIR = os.getcwd()


"""
selenium资料

size 获取元素的尺寸
text 获取元素的文本
get_attribute(name) 获取属性值
location 获取元素坐标，先找到要获取的元素，再调用该方法
page_source 返回页面源码
driver.title 返回页面标题
current_url 获取当前页面的URL
is_displayed() 设置该元素是否可见
is_enabled() 判断元素是否被使用
is_selected() 判断元素是否被选中
tag_name 返回元素的tagName

调用举例
page = Pager()
page_list = page.list_page_links("http://www.dianping.com/search/category/8/75/g2872")
page.get_item_info(page_list["items"][0])
"""
class Pager(object):
    def __init__(self):
        # 初始化浏览器
        # 设置浏览器代理，讲非dianping.com的其它请求代理到本地，禁止访问
        myweb="127.0.0.1"
        myport=80

        profile=webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", myweb)
        profile.set_preference("network.proxy.http_port", myport)
        profile.set_preference("network.proxy.no_proxies_on", 'localhost, 127.0.0.1, dianping.com')

        br = webdriver.Firefox(profile)
        br.maximize_window()
        self.br = br
        self.base_url = "http://www.dianping.com"

    # 获取下一页的地址，以及当前页所有的商铺链接
    def list_page_links(self, url):
        result = {}
        result["next_page"] = ""
        result["items"] = []

        print url
        self.br.implicitly_wait(30)

        self.br.set_page_load_timeout(10)
        try:
            print "开始加载..."
            self.br.get(url)
            print "加载完成..."
        except Exception,e:
            print 'time out after 10 seconds when loading page'
            self.br.execute_script('window.stop()')
            #当页面加载时间超过设

        cur_page = self.br.find_elements_by_xpath("//div[@class='page']/a[@class='cur']")
        cur_page_num = int(cur_page[0].text)
        if cur_page_num < 50:
            next_page_num = cur_page_num + 1
            # 下一页的地址
            next_page_links = self.br.find_elements_by_xpath("//div[@class='page']/a[@data-ga-page='%d']"%next_page_num)
            next_page_url = next_page_links[0].get_attribute("href")
            result["next_page"] = next_page_url
            print next_page_url
            # 商铺链接
            shops_xpath = "//div[@id='shop-all-list']/ul/li/div[@class='txt']/div[@class='tit']/a[1]"
            shop_links = self.br.find_elements_by_xpath(shops_xpath)
            for shop_link in shop_links:
                result["items"].append(shop_link.get_attribute("href"))
                print shop_link.get_attribute("href")
        else:
            print "================>最后一页"
        return result

    # 获取商铺详情页信息
    def get_item_info(self, url):
        #url = "http://www.dianping.com/shop/65997732"
        print url

        result = {}
        result["title"] = ""
        result["phone"] = ""
        result["address"] = ""
        result["description"] = ""
        result["url"] = url

        dr = re.compile(r'<[^>]+>',re.S)
        parser = HTMLParser.HTMLParser()

        time.sleep(random.uniform(0, 2))

        self.br.set_page_load_timeout(10)
        try:
            print "开始加载..."
            self.br.get(url)
            print "加载完成..."
        except Exception,e:
            print 'time out after 10 seconds when loading page'
            self.br.execute_script('window.stop()')
            #当页面加载时间超过设定时间，通过执行Javascript来stop加载，即可执行后续动作


        # 匹配标题
        shop_title_xpath = u"//div[@class='breadcrumb']/div[@class='inner']/span|//div[@class='breadcrumb']/strong|//div[@class='breadcrumb']/span"
        shop_titles = self.br.find_elements_by_xpath(shop_title_xpath)
        title = shop_titles[0].text
        result["title"] = title.encode("utf-8")
        print title.encode("utf-8")


        # 匹配地址
        shop_address_xpath = u"//div[@class='brief-info']/div[@class='address']|//div[@class='shop-info']/div[@class='shop-addr']/span|//div[@itemprop='street-address']"
        shop_addresses = self.br.find_elements_by_xpath(shop_address_xpath)
        address_str = shop_addresses[0].get_attribute("innerHTML")
        address_str = dr.sub('', address_str)
        result["address"] = parser.unescape(address_str).encode("utf-8")
        print result["address"]

        # 匹配电话
        shop_phone_xpath = u"//div[@class='book']/div[@class='phone']/span|//div[@class='shop-info']/div[@class='shopinfor']/p/span[1]|//span[@itemprop='tel']"
        print "开始匹配电话..."
        shop_phones = self.br.find_elements_by_xpath(shop_phone_xpath)
        print "匹配电话完成..."
        if shop_phones:
            shop_phone = shop_phones[0].text
            result["phone"] = shop_phone.encode("utf-8")
            print result["phone"]

        # 匹配简介
        if result["phone"]:
            shop_desc_xpath = u"//div[@class='mod-wrap']/div[@id='info']/ul/li[2]|//div[@class='con J_showWarp']/div[@class='block_all']/div[2]/span"
            print "开始匹配简介..."
            shop_descs = self.br.find_elements_by_xpath(shop_desc_xpath)
            print "匹配简介完成..."
            if shop_descs:
                shop_desc_str = shop_descs[0].get_attribute("innerHTML")
                shop_desc_str = dr.sub('', shop_desc_str)
                result["description"] = parser.unescape(shop_desc_str).encode("utf-8")
                print result["description"]
        print "全部完成..."

        return result
