#!/usr/bin/env python
#coding=utf-8

'''
@Desc
    维护三个队列：
    FloorQueue     存放一级目录 url 链接的队列
    MiddleQueue    存放二级目录 url 链接的队列
    ContentQueue   存放获取电影信息(名称、导演、主角、下载地址等)的队列, 方便后续持久化

    存放未爬取 url 的队列
    存放
@Author monkey
@Date 2017-08-11
'''
from queue import Queue


class TaskQueue(object):

    floorQueue = Queue()
    middleQueue = Queue()
    contentQueue = Queue()

    def __init__(self):
        pass

    # get queue
    @classmethod
    def getFloorQueue(cls):
        return cls.floorQueue

    @classmethod
    def getMiddleQueue(cls):
        return cls.middleQueue

    @classmethod
    def getContentQueue(cls):
        return cls.contentQueue

    # Return True if the queue is empty, False otherwise (not reliable!).
    @classmethod
    def isFloorQueueEmpty(cls):
        return cls.floorQueue.empty()

    @classmethod
    def isMiddleQueueEmpty(cls):
        return cls.middleQueue.empty()

    @classmethod
    def isContentQueueEmpty(cls):
        return cls.contentQueue.empty()

    # Put an item into the queue.
    @classmethod
    def putToFloorQueue(cls, item):
        cls.floorQueue.put(item)

    @classmethod
    def putToMiddleQueue(cls, item):
        cls.middleQueue.put(item)

    @classmethod
    def putToContentQueue(cls, item):
        cls.contentQueue.put(item)
