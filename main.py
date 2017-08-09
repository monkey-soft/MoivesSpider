#!/usr/bin/env python
#coding=utf-8


from queue import Queue

from FloorWorkThread import WorkThread
from dytt8.dytt8Moive import dytt_Lastest

'''
    程序主入口
@Author monkey
@Date 2017-08-08
'''

# 截止到2017-08-08, 最新电影一共才有 164 个页面
LASTEST_MOIVE_TOTAL_SUM = 164

# 线程总数
THREAD_SUM = 10


def startSpider():
    # 实例化对象
    dyttlastest = dytt_Lastest(LASTEST_MOIVE_TOTAL_SUM)
    floorlist = dyttlastest.getPageUrlList()

    floorQueue = Queue()
    for item in floorlist:
        floorQueue.put(item, 3)

    print(floorQueue.qsize())

    for i in range(THREAD_SUM):
        workthread = WorkThread(floorQueue, i)
        workthread.start()
        # workthread.join()


if __name__ == '__main__':
    startSpider()