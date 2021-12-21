# # '''
# # 程序思路：
# # 1.导入包 工具 库
# # 2.获取数据
# # 3.解析数据 音乐
# # 4.保存数据 本地文件夹
# # '''
# import requests
# from lxml import etree  # 解析数据
# import json
#
# # 目标网址 url网址
# url = 'https://music.163.com/#/discover/toplist?id=19723756'
# url_base = 'http://music.163.com/song/media/outer/url?id='
# headers = {
#     'user-agent': 'Mozilla/5.0'
# }
# url = url.replace(r"/#", "")
# r = requests.get(url, headers=headers)
# html = etree.HTML(r.text)
# # id_list = html.xpath('//a[contains(@href,"/song?id=")]')
# id_list = html.xpath('//ul[class="f-hide"]//a/@href')
# print(id_list)
# for data in id_list:
#     href = data.xpath('./@href')[0]
#     music_id = href.split("=")[1]
#     music_name = data.xpath('./text()')[0]
#     music_url = url_base + music_id
#     print(music_url)
#     music = requests.get(music_url, headers=headers)
#
#     with open('C:/Users/86153/Desktop/musics/'+music_name+'.mp3', 'wb') as file:
#         file.write(music.content)
#         print('<%s>  成功' % music_name)

# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os
import re
import time
from random import randint

BASE_ID = []
TOP_NAME = []
MUSIC_NAME = []
MUSIC_URL = []

# 网址
# 解析页面
# 下载
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; "
    ".NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR "
    "2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR "
    "3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; "
    ".NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR "
    "3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 ("
    "Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 "
    "Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]
Headers = {
    'User-Agent': random_agent,
    "referer": "https://music.163.com/"
}


def parse_page(url):
    req = requests.get(url, headers=Headers)
    text = req.text
    html = etree.HTML(text)
    id_tags = html.xpath('//ul[@class="f-hide"]//a/@href')
    for id_tag in id_tags:
        music_id = id_tag.replace("/song?id=", "")
        BASE_ID.append(music_id)  # 获取到每一个id并加到列表中
    top_names = html.xpath('//div[@class="hd f-cb"]/h2/text()')
    for top_name in top_names:
        TOP_NAME.append(top_name)
    music_names = html.xpath('//ul[@class="f-hide"]//a/text()')
    for music_name in music_names:
        music_name = re.sub(r'[\?？\.。!！\*]', '', music_name)
        MUSIC_NAME.append(music_name)


def parse_url():
    print("*" * 12 + "音乐下载位置在（桌面->musics文件夹）中" + "*" * 12)
    print("**" * 10 + "请输入排行榜的url" + "**" * 10)
    url = input()
    url = url.replace(r"/#", "")
    toplist_url = url  # 不是原网址，原网址找不到id
    base_url = "http://music.163.com/song/media/outer/url?id={}"
    parse_page(toplist_url)
    for id in BASE_ID:
        music_url = base_url.format(id)
        MUSIC_URL.append(music_url)


def dowmloads():
    z = 0
    path = "C:/Users/86153/Desktop/musics/%s" % TOP_NAME[0]
    print("*" * 16 + "%s开始下载" % TOP_NAME[0] + "*" * 16)
    if not os.path.exists(path):
        os.makedirs(path)
    for x, y in zip(MUSIC_URL, MUSIC_NAME):
        req = requests.get(x, headers=Headers).content
        with open(("%s\%s.mp3" % (path, y)), 'wb')as f:
            f.write(req)
            print("《%s》下载完成" % y)
        z = z + 1
        if (z % 5 == 0):
            time.sleep(1)


if __name__ == '__main__':
    try:
        parse_url()
        dowmloads()
    except:
        print('这首歌爬取失败。')
