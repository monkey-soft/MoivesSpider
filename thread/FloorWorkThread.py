#!/usr/bin/env python
#coding=utf-8

import threading
import time

import requests

from dytt8.dytt8Moive import dytt_Lastest
from model.RequestModel import RequestModel
from model.TaskQueue import TaskQueue

'''
    1)自己封装抓取二级网页多线程
    2)由一级链接 抓取 电影目录
    例如：由 http://www.dytt8.net/html/gndy/dyzz/list_23_2.html 获取
           "2017年动画喜剧《宝贝老板》英国粤三语.BD中英双字幕" 和 "页面 url 地址"等若干条电影的信息
@Author monkey
@Date 2017-08-08
'''

class FloorWorkThread(threading.Thread):

    NOT_EXIST = 0

    host = 'http://www.dytt8.net'

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
                break

            url = self.queue.get()
            try:
                response = requests.get(url, headers=RequestModel.getHeaders(), proxies=RequestModel.getProxies(), timeout=3)
                print('Floor 子线程 ' + str(self.id) + ' 请求【 ' + url + ' 】的结果： ' + str(response.status_code))

                # 需将电影天堂的页面的编码改为 GBK, 不然会出现乱码的情况
                response.encoding = 'GBK'

                if response.status_code != 200:
                    self.queue.put(url)
                    time.sleep(20)
                else :
                    moivePageUrlList = dytt_Lastest.getMoivePageUrlList(response.text)
                    for item in moivePageUrlList:
                        each = self.host + item
                        # print(each)
                        TaskQueue.putToMiddleQueue(each)
                time.sleep(3) # 5

            except Exception as e:
                # print('catsh  Exception ==== ')
                self.queue.put(url)
                print(e)