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

from model.RequestModel import RequestModel


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
        selector = etree.HTML(html)
        templist = selector.xpath("//div[@class='co_content8']/ul/td/table/tr/td/b/a/@href")
        # print(len(templist))
        # print(templist)
        return templist

    @classmethod
    def getMoiveInforms(cls, url, html):
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
        ◎简介      : 暂不要该字段
        ◎获奖情况   : 暂不要该字段
        ◎海报
        影片截图
        下载地址
        '''
        # print(html)
        contentDir = {
            'type': '',
            'trans_name': '',
            'name': '',
            'decade': '',
            'conutry': '',
            'level': '',
            'language': '',
            'subtitles': '',
            'publish': '',
            'IMDB_socre': '',
            'douban_score': '',
            'format': '',
            'resolution': '',
            'size': '',
            'duration': '',
            'director': '',
            'actors': '',
            'placard': '',
            'screenshot': '',
            'ftpurl': '',
            'dytt8_url': ''
        }

        selector = etree.HTML(html)
        content = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/td/p/text()")
        # 匹配出来有两张图片, 第一张是海报, 第二张是电影画面截图
        imgs = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/td/p/img/@src")
        # print(content)

        # 为了兼容 2012 年前的页面
        if not len(content):
            content = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/span/text()")

        # 有些页面特殊, 需要用以下表达式来重新获取信息
        # 电影天堂页面好混乱啊~
        if not len(content):
            content = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/td/div/text()")

        if not len(content):
            content = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/p/font/text()")
            if len(content) < 5:
                content = selector.xpath("//div[@class='co_content8']/ul/tr/td/p/font/text()")

        if not len(content):
            content = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/p/span/text()")

        if not len(content):
            content = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/div/span/text()")

        if not len(content):
            content = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/font/text()")

        if not len(content):
            content = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/p/text()")

        # print(content)

        # 不同渲染页面要采取不同的抓取方式抓取图片
        if not len(imgs):
            imgs = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/img/@src")

        if not len(imgs):
            imgs = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/p/img/@src")

        if not len(imgs):
            imgs = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/div/img/@src")

        if not len(imgs):
            imgs = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/td/div/img/@src")

        # 类型
        if content[0][0:1] != '◎':
            contentDir['type'] = '[' + content[0]
        actor = ''

        for each in content:
            if each[0:5] == '◎译\u3000\u3000名':
                # 译名 ◎译\u3000\u3000名\u3000  一共占居6位
                contentDir['trans_name'] = each[6: len(each)]
            elif each[0:5] == '◎片\u3000\u3000名':
                # 片名
                contentDir['name'] = each[6: len(each)]
            elif each[0:5] == '◎年\u3000\u3000代':
                # 年份
                contentDir['decade'] = each[6: len(each)]
            elif each[0:5] == '◎产\u3000\u3000地':
                # 产地
                contentDir['conutry'] = each[6: len(each)]
            elif each[0:5] == '◎类\u3000\u3000别':
                # 类别
                contentDir['level'] = each[6: len(each)]
            elif each[0:5] == '◎语\u3000\u3000言':
                # 语言
                contentDir['language'] = each[6: len(each)]
            elif each[0:5] == '◎字\u3000\u3000幕':
                # 字幕
                contentDir['subtitles'] = each[6: len(each)]
            elif each[0:5] == '◎上映日期':
                # 上映日期
                contentDir['publish'] = each[6: len(each)]
            elif each[0:7] == '◎IMDb评分':
                # IMDb评分
                contentDir['IMDB_socre'] = each[9: len(each)]
            elif each[0:5] == '◎豆瓣评分':
                # 豆瓣评分
                contentDir['douban_score'] = each[6: len(each)]
            elif each[0:5] == '◎文件格式':
                # 文件格式
                contentDir['format'] = each[6: len(each)]
            elif each[0:5] == '◎视频尺寸':
                # 视频尺寸
                contentDir['resolution'] = each[6: len(each)]
            elif each[0:5] == '◎文件大小':
                # 文件大小
                contentDir['size'] = each[6: len(each)]
            elif each[0:5] == '◎片\u3000\u3000长':
                # 片长
                contentDir['duration'] = each[6: len(each)]
            elif each[0:5] == '◎导\u3000\u3000演':
                # 导演
                contentDir['director'] = each[6: len(each)]
            elif each[0:5] == '◎主\u3000\u3000演':
                # 主演
                actor = each[6: len(each)]

        for item in content:
            if item[0: 4] == '\u3000\u3000\u3000\u3000':
                actor = actor + '\n' + item[6: len(item)]

        # 主演
        contentDir['actors'] = actor
        # 海报
        if imgs[0] != None:
            contentDir['placard'] = imgs[0]
        # 影片截图
        if imgs[1] != None:
            contentDir['screenshot'] = imgs[1]
        # 下载地址
        ftp = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/td/table/tbody/tr/td/a/text()")

        # 为了兼容 2012 年前的页面
        if not len(ftp):
            ftp = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/table/tbody/tr/td/font/a/text()")

        if not len(ftp):
            ftp = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/table/tbody/tr/td/a/text()")

        if not len(ftp):
            ftp = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/div/table/tbody/tr/td/font/a/text()")

        if not len(ftp):
            ftp = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/td/div/table/tbody/tr/td/a/text()")

        if not len(ftp):
            ftp = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/td/table/tbody/tr/td/a/text()")

        if not len(ftp):
            ftp = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/p/span/a/text()")

        if not len(ftp):
            ftp = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/div/div/table/tbody/tr/td/font/a/text()")

        if not len(ftp):
            ftp = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/span/table/tbody/tr/td/font/a/text()")

        if not len(ftp):
            ftp = selector.xpath("//div[@class='co_content8']/ul/tr/td/div/div/td/div/span/div/table/tbody/tr/td/font/a/text()")

        contentDir['ftpurl'] = ftp[0]
        # 页面链接
        contentDir['dytt8_url'] = url
        print(contentDir)
        return contentDir