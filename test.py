#coding:utf-8
import time
import os

def logger(log):
    os.system("echo %s >> /home/aaoo/114_log/test.log" % log)

for i in range(1170):
    log = time.strftime("[%Y-%m-%d %H:%M:%S]",time.localtime(time.time()))
    logger(log)
    os.system("python /home/aaoo/桌面/114/here114/page_114.py")
    time.sleep(1)

logger("ok")
