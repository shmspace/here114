#coding:utf-8
import time
import os

def logger(log):
    os.system("echo %s >> /tmp/test.log" % log)

for i in range(1170):
    log = time.strftime("[%Y-%m-%d %H:%M:%S]",time.localtime(time.time()))
    logger(log)
    os.system("flock -xn /tmp/page_114_aaoo.lock -c 'python /home/aaoo/桌面/114/here114/page_114.py >/dev/null 2>&1'")
    time.sleep(1)

logger("ok")
