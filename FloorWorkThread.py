#!/usr/bin/env python
#coding=utf-8
import threading
import requests
import time

from RequestModel import RequestModel

'''
    1)自己封装抓取二级网页多线程
    2)由一级链接 抓取 电影目录
    例如：由 http://www.dytt8.net/html/gndy/dyzz/list_23_2.html 获取
           "2017年动画喜剧《宝贝老板》英国粤三语.BD中英双字幕"等若干条电影的信息
@Author monkey
@Date 2017-08-08
'''

class WorkThread(threading.Thread):

    NOT_EXIST = 0

    def __init__(self, queue, id):
        threading.Thread.__init__(self)
        self.queue = queue
        self.id = id


    def run(self):
        while not self.NOT_EXIST:
            # 队列为空, 结束
            if self.queue.empty():
                NOT_EXIST = 1
                self.queue.task_done()
                break;

            try:
                url = self.queue.get()
                print(url)
                html = requests.get(url, headers=RequestModel.getHeaders(), proxies=RequestModel.getProxies(), timeout=3)
                print('线程id ' + str(self.id) + ' 请求的结果： '  + str(html.status_code))
                time.sleep(1)
            except Exception as e:
                # print('catsh  Exception ==== ')
                print(e)

