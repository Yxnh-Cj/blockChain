# from bs4 import BeautifulSoup
# import requests
# from lxml import etree
# from 翻译 import trans
# import cv
# import matplotlib
#
# headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/95.0.4636.4 Safari/537.36', 'referer': 'https://www.pexels.com/' } url_path =
# 'https://www.pexels.com/search/' content = input('请输入你要搜索的内容:') url = url_path+trans(content).replace(' ',
# '%20')+'/' wb_data = requests.get(url,headers=headers) soup = BeautifulSoup(wb_data.text,'html.parser') imgs =
# soup.select('article > a > img') list = [] for img in imgs: photo = img.get('src') list.append(photo) print(list)
# path = 'C:/Users/86153/Desktop/photo/' for item in list: data = requests.get(item,headers=headers) fp = open(
# path+item.split('?')[0][-10:],'wb') fp.write(data.content) fp.close()
# -*- coding: utf-8 -*-
# import requests
# from bs4 import BeautifulSoup
# import json
#
# url = 'https://www.pexels.com/zh-cn/search/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (XHTML, like Gecko) '
#                          'Chrome/96.0.4664.45 Safari/537.36'}
# s = input('输入查找内容:')
# res = requests.get(url+s+'/', headers=headers)
# print(res.status_code)  # 403禁止访问
# soup = BeautifulSoup(res.text,'lxml')
# print(soup.prettify())
# imgs = soup.select('body > div.page-wrap > div.search > div.search__grid > div.photos > div:nth-child(1) > '
#                    'div:nth-child(1) > article ')
# print(imgs)
'''
400-请求无效
说明服务器无法理解用户的请求，除非进行修改，不然你按再多刷新也没有用。很有可能的情况是，你不小心输入错误了，导致服务器根本不知道你要表达什么。

认真检查有没有无输入
403-禁止访问
出现403是因为服务器拒绝了你的地址请求，很有可能是你根本就没权限访问网站，就算你提供了身份验证也没用。讲真，很有可能是你被禁止访问了。

除非你与Web服务器管理员联系，否则一旦遇到403状态码都无法自行解决。
404-无法找到文件
404其实在日常生活中很常见了。代码的意思是找不到要查询的页面。非常有可能是网页被删除了。
405-资源被禁止
资源被禁止，有可能是文件目录权限不够导致的。这个时候其实，只要赋予“完全控制”的权限，也是可以解决的
408-请求超时
遇到408意味着你的请求发送到该网站花的时间比该网站的服务器准备等待的时间要长，即链接超时。
305-使用代理
这个代码的意思是，你不能直接访问网站，要通过某个代理才能进去。

比如，你想要访问一些外网，一定要使用VPN才可以。
'''

# import requests
# from bs4 import BeautifulSoup
# import time
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (XHTML, like Gecko) '
#                          'Chrome/96.0.4664.45 Safari/537.36'}
# res = requests.get('https://www.jd.com/',headers = headers)
# soup = BeautifulSoup(res.text,'lxml')
# im = soup.select('#J_cate > ul > li:nth-child(2) > a:nth-child(1)')
# im_new = str(im)
# url_new = 'https:'+im_new.split(' ')[2].split('=')[1].replace('"','')
# time.sleep(0.5)
# res_new = requests.get(url_new,headers = headers)
# soup = BeautifulSoup(res_new.text,'lxml')
# time.sleep(0.5)
# response = soup.select('#app > div > div.lc-floor.lc-xfloor--id-1597905420432.lc-floor--lg > div > div > '
#                        'div.lc-col.lc-col--cols6-1 > div > div:nth-child(1) > div > div > div > div > '
#                        'div.quark-5cb43f1780772100479b2052__nav-channel__header > ul > li:nth-child(1) > nav > '
#                        'a:nth-child(1)')
# print(response)

import requests

url = "https://images.pexels.com/photos/768262/pexels-photo-768262.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
headers_ = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.45 Safari/537.36 '
}
response = requests.get(url,headers=headers_)

bytes_data = response.content
with open('pexels图片/图片.jpg', 'wb') as f:
    f.write(bytes_data)