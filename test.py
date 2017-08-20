import requests
import sqlite3

from RequestModel import RequestModel
from TaskQueue import TaskQueue

'''
@Desc
    测试各个功能的脚本

@Author monkey
@Date 2017-08-08
'''

# 测试案例1
# url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_2.html'
# html = requests.get(url, headers=RequestModel.getHeaders(), proxies=RequestModel.getProxies())
# print(html.status_code)

# 测试案例2
DBName = 'dytt.db'
db = sqlite3.connect('./'+DBName, 10)
conn = db.cursor()

SelectSql = 'select * from sqlite_master where type = "table" and name="latest_moive";'
CreateTableSql = '''
    Create Table lastest_moive (
        'm_id' int auto_increment,
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
#            'm_synopsis' varchar(5000),
#           'm_prize' varchar(5000),
        'm_placard' varchar(200),
        'm_screenshot' varchar(200),
        'm_ftpurl' varchar(200)
    );
'''
InsertSql = ''

if not conn.execute(SelectSql).fetchone():
    conn.execute(CreateTableSql)
    db.commit()
    print('====  创建表成功  ====')
else :
    print('====  创建表失败, 表已经存在  ====')

# count = 1
# while TaskQueue.isContentQueueEmpty():
#     item = TaskQueue.getContentQueue().get()
#     conn.execute(InsertSql)
#     db.commit()
#     print('插入第 ' + str(count) + ' 条数据成功')
#     count = count + 1
#
# db.commit()
# db.close()