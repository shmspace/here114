#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys #引入keys类操作

import os
import time

ROOT_DIR = os.getcwd()

class Pager(object):
    def __init__(self):
        br = webdriver.Firefox()
        br.maximize_window()
        self.br = br

    def list_page_links(self, url):
        result = {}
        result["next_page"] = ""
        result["items"] = []

        print url
        self.br.implicitly_wait(30)
        self.br.get(url)
        print "1111"
        #self.br.implicitly_wait(3)
        print "2222"
        pages = self.br.find_elements_by_xpath("//div[@class='page']/a[@class='cur']")
        print "3333"
        print pages[0].text
        print "======="

page = Pager()
page.list_page_links("http://www.dianping.com/search/category/8/75/g2872")


