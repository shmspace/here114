#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys #引入keys类操作

import os
import time
import signal
import types

import xlrd
import xlwt as ExcelWrite

import urllib2
import urllib
import json

ROOT_DIR = os.getcwd()

class Pager(object):
    def __init__(self):
        pass

    def init_br(self, url):
        br = webdriver.Firefox()
        br.implicitly_wait(30)
        br.maximize_window()
        self.br = br
        self.url = url
        self.br.get(self.url)

    def get_info(self, phone):
        phone_input = self.br.find_elements_by_xpath("//input[@name='Keywords']")
        phone_input[0].clear()
        phone_input[0].send_keys(phone)

        search_input = self.br.find_elements_by_xpath("//img[@src='../images/button_search.gif']")
        search_input[0].click()
        self.br.implicitly_wait(30)

        name, phone, address = "","",""
        a_line = self.br.find_element_by_xpath("id('A')/td[1]")
        if a_line.get_attribute('id') == "A1":
            name = self.br.find_element_by_xpath("id('A2')").text
            phone = self.br.find_element_by_xpath("id('A3')").text
            address = self.br.find_element_by_xpath("id('A4')").text
        return name.encode("utf-8"), phone, address.encode("utf-8")

    def check_name(self, old_name, name):
        all_num = len(name)
        check_num = 0
        for i in range(0, len(name)):
            for j in range(0, len(old_name)):
                if name[i] == old_name[j]:
                    check_num = check_num + 1
                    break
        if check_num == 0:
            percent = 0
        else:
            percent = check_num * 100 / all_num
        return percent

class ExcelManage(object):
    def __init__(self):
        self.category = 0
        self.name = 1
        self.address = 2
        self.phone = 3
        self.source = 4

    def load(self, file_name):
        workbook = xlrd.open_workbook(file_name)
        sheet = workbook.sheet_by_index(0)
        self.sheet = sheet

    def nrows(self):
        return self.sheet.nrows

    def get_info(self, i):
        sheet = self.sheet
        category = sheet.row_values(i)[self.category].encode("utf-8")
        name = sheet.row_values(i)[self.name].encode("utf-8")
        address = sheet.row_values(i)[self.address].encode("utf-8")
        cur_phone = phone = sheet.row_values(i)[self.phone]
        if type(phone) == types.FloatType:
            phone = str(int(phone))
        if type(phone) == types.IntType:
            phone = str(phone)
        phone = self.format_phone(phone)
        source = sheet.row_values(i)[self.source].encode("utf-8")
        return category, name, address, phone, source, cur_phone

    def format_phone(self, phone):
        phones = phone.split(" ")
        if len(phones) == 1:
            phones = phone.split(",")
        if len(phones) == 1:
            phones = phone.split("|")
        for i in range(0, len(phones)):
            tphone = phones[i]
            if tphone[0:4] == "028-":
                tphone = tphone[4:100]
            if tphone[0:5] == "(028)":
                tphone = tphone[5:100]
            if tphone[0:3] == "028":
                tphone = tphone[3:100]
            phones[i] = tphone
        return phones

def format_phone(phone):
    real_phone = []
    phones = phone.split(" ")
    if len(phones) == 1:
        phones = phone.split(",")
    if len(phones) == 1:
        phones = phone.split("|")
    for i in range(0, len(phones)):
        tphone = phones[i]
        if tphone[0:4] == "028-":
            tphone = tphone[4:100]
            real_phone.append(tphone)
        if tphone[0:5] == "(028)":
            tphone = tphone[5:100]
            real_phone.append(tphone)
        if tphone[0:3] == "028":
            tphone = tphone[3:100]
            real_phone.append(tphone)
        if tphone[0:1] == "1":
            tphone = tphone[0:11]
            real_phone.append(tphone)
        try:
            if str(int(tphone)) == tphone:
                real_phone.append(tphone)
        except Exception, e:
            pass
    return real_phone



def find_item_from_server(from_id):
    server_url = "http://123.207.1.180:8080"
    url = "%s/index.php?r=api/site/find&max_id=%d&limit=500" % (server_url, from_id)
    logger(url)
    req = urllib2.urlopen(url)
    logger("Item 数据发送服务器保存成功......")
    result = req.read()
    reqs = json.loads(result)
    return reqs

def handler(signum, frame):
    logger("timeout!")
    raise SystemExit("exit.....")

def logger(log):
    os.system("echo %s >> /tmp/test.log" % str(log))

