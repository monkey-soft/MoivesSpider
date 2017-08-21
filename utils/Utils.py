#!/usr/bin/env python
#coding=utf-8

'''
    工具类
@Author monkey
@Date 2017-08-21
'''

class Utils(object):

    '''
    将字典转化为列表
    '''
    @staticmethod
    def dirToList(item):
        itemlist = []
        itemlist.append(item['type'])
        itemlist.append(item['trans_name'])
        itemlist.append(item['name'])
        itemlist.append(item['decade'])
        itemlist.append(item['conutry'])
        itemlist.append(item['level'])
        itemlist.append(item['language'])
        itemlist.append(item['subtitles'])
        itemlist.append(item['publish'])
        itemlist.append(item['IMDB_socre'])
        itemlist.append(item['douban_score'])
        itemlist.append(item['format'])
        itemlist.append(item['resolution'])
        itemlist.append(item['size'])
        itemlist.append(item['duration'])
        itemlist.append(item['director'])
        itemlist.append(item['actors'])
        itemlist.append(item['placard'])
        itemlist.append(item['screenshot'])
        itemlist.append(item['ftpurl'])
        itemlist.append(item['dytt8_url'])
        return itemlist