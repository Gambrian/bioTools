# -*- coding = utf-8 -*- 
# @Time : 2022/3/10 10:46
# @Author : YJ Geng
# @File : test.py
# @Software : PyCharm


from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def test():
    msg = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("hello world! " + msg)


scheduler = BlockingScheduler()
scheduler.add_job(test, 'cron', day_of_week='1-5', hour=10, minute=53)
scheduler.start()
