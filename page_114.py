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

    def get_info(self, phone, code):
        phone_input = self.br.find_elements_by_xpath("//input[@name='Keywords']")
        phone_input[0].clear()
        phone_input[0].send_keys(phone)

        self.select_by_value(code)

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

    def select_by_value(self, code):
        select_el = self.br.find_element_by_xpath("//select[@name='area_code']/option[@value='SC']")
        select_el.click()

        select_el = self.br.find_element_by_xpath("//select[@name='area_code']/option[@value='"+ code +"']")
        select_el.click()

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
        if tphone[0:5] == "(028)":
            tphone = tphone[5:100]
        if tphone[0:3] == "028":
            tphone = tphone[3:100]
        if tphone[0:1] == "1":
            tphone = tphone[0:11]

        area_list = ["0816-", "0833-", "0838-", "0817-", "0818-", "0830-", "0831-", "0832-", "0813-", "0826-"]
        if tphone[0:5] in area_list:
            tphone = tphone[5:100]

        area_list = ["(0816)", "(0833)", "(0838)", "(0817)", "(0818)", "(0830)", "(0831)", "(0832)", "(0813)", "(0826)"]
        if tphone[0:6] in area_list:
            tphone = tphone[6:100]

        area_list = ["0816", "0833", "0838", "0817", "0818", "0830", "0831", "0832", "0813", "0826"]
        if tphone[0:4] in area_list:
            tphone = tphone[4:100]

        try:
            if str(int(tphone)) == tphone:
                real_phone.append(tphone)
        except Exception, e:
            pass
    return real_phone

def find_area(category):
    code = "SC"
    if u"绵阳" in category:
        code = "SCMY"
    if u"乐山" in category:
        code = "SCLS"
    if u"德阳" in category:
        code = "SCDY"
    if u"南充" in category:
        code = "SCNC"
    if u"达州" in category:
        code = "SCDC"
    if u"泸州" in category:
        code = "SCLZ"
    if u"宜宾" in category:
        code = "SCYB"
    if u"内江" in category:
        code = "SCNJ"
    if u"资阳" in category:
        code = "SCZY"
    if u"自贡" in category:
        code = "SCZG"
    if u"眉山" in category:
        code = "SCMS"
    if u"广安" in category:
        code = "SCGA"
    return code

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
    os.system("echo %s >> /home/aaoo/114_log/test.log" % str(log))

os.system("killall firefox")

signal.signal(signal.SIGALRM, handler)

need_percent = 50

settings = "/home/aaoo/114_log/current_id.txt"
try:
    handle = open(settings, "r")
    i = int(handle.read())
    handle.close()
except:
    i = int(raw_input("输入起始id: "))

while 1:
    url = "http://133.37.92.17:8083/besttone/agent/businessMainAction.do?action=hmfc"
    handle = open(settings, "w")
    handle.write(str(i)) 
    handle.close()

    items = find_item_from_server(i)
    rows = []
    page = Pager()
    page.init_br(url)
    output_xls = "/home/aaoo/桌面/excel/output_data10_%s.xls" % i
    for item in items:
        i = item["id"]

        logger(time.strftime("[%Y-%m-%d %H:%M:%S]",time.localtime(time.time())))
        logger(item["id"])

        name = item["name"]
        address = item["adress"]
        cur_phone = item["phone"]
        source = item["item_url"]
        phone = format_phone(item["phone"])
        code = find_area(item["category"])
        if len(phone) == 0:
            continue
        for j in range(0, len(phone)):
            while 1:
                try:
                    signal.alarm(30)
                    old_name, old_phone, old_address = page.get_info(phone[j], code)
                    signal.alarm(0)
                    break
                except Exception, e:
                    signal.alarm(0)
                    time.sleep(5)
                    logger("error!")
            percent = page.check_name(old_name, name)
            if old_name != '':
                break
        row = {}
        row["category"] = item["category"]
        row["id"] = item["id"]
        row["name"] = name
        row["address"] = address
        row["cur_phone"] = cur_phone
        row["source"] = source
        row["old_name"] = old_name
        row["old_phone"] = old_phone
        row["old_address"] = old_address
        row["percent"] = percent
        if percent >= need_percent:
            row["status"] = "ok"
        else:
            if row["old_name"] != '':
                row["status"] = "update"
            else:
                row["status"] = "check_name"
        rows.append(row)

    page.br.close()
    page.br.quit()

    # 检查地址
    url_address = "http://133.37.92.17:8083/besttone/agent/businessMainAction.do?action=hxxx"
    page_address = Pager()
    page_address.init_br(url_address)

    for n in range(0, len(rows)):
        row = rows[n]
        logger(time.strftime("[%Y-%m-%d %H:%M:%S]",time.localtime(time.time())))
        logger(n)
        if row["status"] == "check_name":
            while 1:
                try:
                    signal.alarm(60)
                    code = find_area(row["category"])
                    old_name, old_phone, old_address = page_address.get_info(row["name"], code)
                    signal.alarm(0)
                    break
                except Exception, e:
                    signal.alarm(0)
                    time.sleep(5)
                    logger("error!")
                    pass

            if old_name == '':
                row["status"] = "new"
            else:
                row["status"] = "update_phone"
                row["old_name"] = old_name
                row["old_phone"] = old_phone
                row["old_address"] = old_address
            rows[n] = row

    page_address.br.close()
    page_address.br.quit()

    # 保存excel

    xls = ExcelWrite.Workbook()
    sheet = xls.add_sheet("Sheet1")
    
    sheet.write(0, 0, "分类".decode("utf-8"))
    sheet.write(0, 1, "名称".decode("utf-8"))
    sheet.write(0, 2, "地址".decode("utf-8"))
    sheet.write(0, 3, "电话".decode("utf-8"))
    sheet.write(0, 4, "来源".decode("utf-8"))
    sheet.write(0, 5, "系统名称".decode("utf-8"))
    sheet.write(0, 6, "系统电话".decode("utf-8"))
    sheet.write(0, 7, "系统地址".decode("utf-8"))
    sheet.write(0, 8, "status")
    sheet.write(0, 9, "id")
    
    for m in range(0, len(rows)):
        row = rows[m]
        sheet.write(m+1, 0, row["category"])
        sheet.write(m+1, 1, row["name"])
        sheet.write(m+1, 2, row["address"])
        sheet.write(m+1, 3, row["cur_phone"])
        sheet.write(m+1, 4, row["source"])
        sheet.write(m+1, 5, row["old_name"].decode("utf-8"))
        sheet.write(m+1, 6, row["old_phone"].decode("utf-8"))
        sheet.write(m+1, 7, row["old_address"].decode("utf-8"))
        sheet.write(m+1, 8, row["status"])
        sheet.write(m+1, 9, row["id"])

    xls.save(output_xls)

    if len(items) < 100:
        break


