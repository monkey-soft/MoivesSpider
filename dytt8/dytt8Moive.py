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
        解析电影信息页面的内容
        '''
        list = []
        selector = etree.HTML(html)  # tr/tr/td/div/td/p/text()
        content = selector.xpath("//div[@class='co_content8']/ul/")
        print(content)