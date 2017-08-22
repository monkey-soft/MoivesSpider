#!/usr/bin/env python
#coding=utf-8


import sqlite3

from dytt8.dytt8Moive import dytt_Lastest
from model.TaskQueue import TaskQueue
from thread.FloorWorkThread import FloorWorkThread
from thread.TopWorkThread import TopWorkThread
from utils.Utils import Utils

'''
    程序主入口
@Author monkey
@Date 2017-08-08
'''

# 截止到2017-08-08, 最新电影一共才有 164 个页面
LASTEST_MOIVE_TOTAL_SUM = 6 #164

# 请求网络线程总数, 线程不要调太好, 不然会返回很多 400
THREAD_SUM = 5


def startSpider():
    # 实例化对象

    # 获取【最新电影】有多少个页面
    LASTEST_MOIVE_TOTAL_SUM = dytt_Lastest.getMaxsize()
    print('【最新电影】一共  ' + str(LASTEST_MOIVE_TOTAL_SUM) + '  有个页面')
    dyttlastest = dytt_Lastest(LASTEST_MOIVE_TOTAL_SUM)
    floorlist = dyttlastest.getPageUrlList()

    floorQueue = TaskQueue.getFloorQueue()
    for item in floorlist:
        floorQueue.put(item, 3)

    # print(floorQueue.qsize())

    for i in range(THREAD_SUM):
        workthread = FloorWorkThread(floorQueue, i)
        workthread.start()

    while True:
        if TaskQueue.isFloorQueueEmpty():
            break
        else:
            pass

    for i in range(THREAD_SUM):
        workthread = TopWorkThread(TaskQueue.getMiddleQueue(), i)
        workthread.start()


    while True:
        if TaskQueue.isMiddleQueueEmpty():
            break
        else:
            pass

    insertData()


def insertData():
    DBName = 'dytt.db'
    db = sqlite3.connect('./' + DBName, 10)
    conn = db.cursor()

    SelectSql = 'Select * from sqlite_master where type = "table" and name="lastest_moive";'
    CreateTableSql = '''
        Create Table lastest_moive (
            'm_id' INTEGER PRIMARY KEY,
            'm_type' varchar(100),
            'm_trans_name' varchar(200),
            'm_name' varchar(100),
            'm_decade' varchar(30),
            'm_conutry' varchar(30),
            'm_level' varchar(100),
            'm_language' varchar(30),
            'm_subtitles' varchar(100),
            'm_publish' varchar(30),
            'm_IMDB_socre' varchar(50),
            'm_douban_score' varchar(50),
            'm_format' varchar(20),
            'm_resolution' varchar(20),
            'm_size' varchar(10),
            'm_duration' varchar(10),
            'm_director' varchar(50),
            'm_actors' varchar(1000),
            'm_placard' varchar(200),
            'm_screenshot' varchar(200),
            'm_ftpurl' varchar(200),
            'm_dytt8_url' varchar(200)
        );
    '''

    InsertSql = '''
        Insert into lastest_moive(m_type, m_trans_name, m_name, m_decade, m_conutry, m_level, m_language, m_subtitles, m_publish, m_IMDB_socre, 
        m_douban_score, m_format, m_resolution, m_size, m_duration, m_director, m_actors, m_placard, m_screenshot, m_ftpurl,
        m_dytt8_url)
        values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''

    if not conn.execute(SelectSql).fetchone():
        conn.execute(CreateTableSql)
        db.commit()
        print('====  创建表成功  ====')
    else:
        print('====  创建表失败, 表已经存在  ====')

    count = 1

    while not TaskQueue.isContentQueueEmpty():
        item = TaskQueue.getContentQueue().get()
        conn.execute(InsertSql, Utils.dirToList(item))
        db.commit()
        print('插入第 ' + str(count) + ' 条数据成功')
        count = count + 1

    db.commit()
    db.close()


if __name__ == '__main__':
    startSpider()