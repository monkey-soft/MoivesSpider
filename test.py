import requests

from RequestModel import RequestModel

'''
@Desc
    测试各个功能的脚本

@Author monkey
@Date 2017-08-08
'''

url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_2.html'
html = requests.get(url, headers=RequestModel.getHeaders(), proxies=RequestModel.getProxies())
print(html.status_code)