#!/usr/bin/env python
#coding=utf-8

'''
@Desc
    主要用来抓取电影天堂（www.dytt8.net）的电影信息(包括电影名、导演、主角、下载地址)
    爬取入口【最新电影】(http://www.dytt8.net/html/gndy/dyzz/index.html)

@Author monkey
@Date 2017-08-08
'''
import requests
from lxml import etree

from RequestModel import RequestModel


class dytt_Lastest(object):

    # 获取爬虫程序抓取入口
    breakoutUrl = 'http://www.dytt8.net/html/gndy/dyzz/index.html'

    def __init__(self, sum):
        self.sum = sum


    # 获取【最新电影】有多少个页面
    # 截止到2017-08-08, 最新电影一共才有 164 个页面
    @classmethod
    def getMaxsize(cls):
        response = requests.get(cls.breakoutUrl, headers=RequestModel.getHeaders(), proxies=RequestModel.getProxies(), timeout=3)
        # 需将电影天堂的页面的编码改为 GBK, 不然会出现乱码的情况
        response.encoding = 'GBK'

        selector = etree.HTML(response.text)
        # 提取信息
        optionList = selector.xpath("//select[@name='sldd']/text()")
        return len(optionList) - 1   # 因首页重复, 所以要减1


    def getPageUrlList(self):
        '''
        主要功能：目录页url取出，比如：http://www.dytt8.net/html/gndy/dyzz/list_23_'+ str(i) + '.html
        '''
        templist = []
        request_url_prefix = 'http://www.dytt8.net/html/gndy/dyzz/'
        templist = [request_url_prefix + 'index.html']

        for i in range(2, self.sum + 1):
            templist.append(request_url_prefix + 'list_23_' + str(i) + '.html')

        for t in templist:
            print('request url is ###   ' + t + '    ###')
        return templist


    @classmethod
    def getMoivePageUrlList(cls, html):
        '''
        获取电影信息的网页链接
        '''
        templist = []
        selector = etree.HTML(html)
        templist = selector.xpath("//div[@class='co_content8']/ul/td/table/tr/td/b/a/@href")
        # print(len(templist))
        # print(templist)
        return templist

    @classmethod
    def getMoiveInforms(cls, html):
        '''
        解析电影信息页面的内容, 具体如下：
        类型        : 疾速特攻/疾速追杀2][BD-mkv.720p.中英双字][2017年高分惊悚动作]
        ◎译名      : ◎译\u3000\u3000名\u3000疾速特攻/杀神John Wick 2(港)/捍卫任务2(台)/疾速追杀2/极速追杀：第二章/约翰·威克2
        ◎片名      : ◎片\u3000\u3000名\u3000John Wick: Chapter Two
        ◎年代　    : ◎年\u3000\u3000代\u30002017
        ◎国家　    : ◎产\u3000\u3000地\u3000美国
        ◎类别　    : ◎类\u3000\u3000别\u3000动作/犯罪/惊悚
        ◎语言　    : ◎语\u3000\u3000言\u3000英语
        ◎字幕　    : ◎字\u3000\u3000幕\u3000中英双字幕
        ◎上映日期  ：◎上映日期\u30002017-02-10(美国)
        ◎IMDb评分  : ◎IMDb评分\xa0 8.1/10 from 86,240 users
        ◎豆瓣评分　 : ◎豆瓣评分\u30007.7/10 from 2,915 users
        ◎文件格式   : ◎文件格式\u3000x264 + aac
        ◎视频尺寸　 : ◎视频尺寸\u30001280 x 720
        ◎文件大小　 : ◎文件大小\u30001CD
        ◎片长　    : ◎片\u3000\u3000长\u3000122分钟
        ◎导演　    : ◎导\u3000\u3000演\u3000查德·史塔赫斯基 Chad Stahelski
        ◎主演　    :
        ◎简介      :
        ◎获奖情况
        ◎海报
        影片截图
        下载地址
        '''
        # print(html)
        contentList = []
        selector = etree.HTML(html)
        content = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/td/p/text()")
        # 匹配出来有两张图片, 第一张是海报, 第二张是电影画面截图
        imgs = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/td/p/img/@src")
        # print(content)
        # 类型
        contentList.append('类型: ' +'['+content[0])
        # 译名
        # ◎译\u3000\u3000名\u3000  一共占居6位
        contentList.append('译名: ' +content[1][6: len(content[1])])
        # 片名
        contentList.append('片名: ' +content[2][6:len(content[2])])
        # 年份
        contentList.append('年份: ' +content[3][6:len(content[3])])
        # 产地
        contentList.append('产地: ' +content[4][6:len(content[4])])
        # 类别
        contentList.append('类别: ' +content[5][6:len(content[5])])
        # 语言
        contentList.append('语言: ' +content[6][6:len(content[6])])
        # 字幕
        contentList.append('字幕: ' +content[7][6:len(content[7])])
        # 上映日期
        contentList.append('上映日期: ' +content[8][6:len(content[8])])
        # IMDb评分
        contentList.append('IMDb评分: ' +content[9][9:len(content[9])])
        # 豆瓣评分
        contentList.append('豆瓣评分: ' +content[10][6:len(content[10])])
        # 文件格式
        contentList.append('文件格式: ' +content[11][6:len(content[11])])
        # 视频尺寸
        contentList.append('视频尺寸: ' +content[12][6:len(content[12])])
        # 文件大小
        contentList.append('文件大小: ' +content[13][6:len(content[13])])
        # 片长
        contentList.append('片长: ' +content[14][6:len(content[14])])
        #　导演
        contentList.append('导演: ' +content[15][5:len(content[15])])
        #　主演
        actor = '主演: ' +content[16][5:len(content[16])]
        for item in content:
            if item[0: 4] == '\u3000\u3000\u3000\u3000':
                actor = actor + '\n'+ item[6: len(item)]

        contentList.append(actor)
        # 海报
        contentList.append(imgs[0])
        # 影片截图
        contentList.append(imgs[1])
        # 下载地址
        ftp = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/td/table/tbody/tr/td/a/text()")
        contentList.append('下载地址: ' +ftp[0])

        for i in  contentList:
            print(i)
        return contentList