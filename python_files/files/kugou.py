# # -*- coding: utf-8 -*-
# import requests
# from bs4 import BeautifulSoup
# import time
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4636.4 Safari/537.36'}
#
# def get_info(url):
#     wb_data = requests.get(url,headers=headers)
#     # soup文档解析方式有:html.parser、lxml、html5lib等（各有优缺点）（来源于python标准库中html标准库中的网页源代码解析调用）
#     soup = BeautifulSoup(wb_data.text,'lxml')
#     ranks = soup.select('span.pc_temp_num')
#     titles = soup.select('div.pc_temp_songlist > ul > li >a')
#     times = soup.select('span.pc_temp_tips_r > span')
#     for rank,title,time in zip(ranks,titles,times):
#         data = {
#             'rank':rank.get_text().strip(),
#             'singer':title.get_text().split('-')[1].strip(),
#             'song':title.get_text().split('-')[0].strip(),
#
#             'time':time.get_text().strip()
#         }
#         print(data)
# if __name__=='__main__':
#     urls = {'http://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in range(1,24)}
#     for url in urls:
#         get_info(url)
#         time.sleep(1)

# from requests_html import HTMLSession
# import urllib.request,os,json
# from urllib.parse import quote
# class KuGou():
#     def __init__(self):
#         self.get_music_url='https://songsearch.kugou.com/song_search_v2?keyword={}&platform=WebFilter'
#         self.get_song_url='https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={}'
#         if not os.path.exists("d:/music"):
#             os.mkdir('d:/music')
#
#     def parse_url(self,url):
#         session = HTMLSession()
#         response = session.get(url)
#         return response.content.decode()
#
#     def get_music_list(self,keyword):
#         music_dirt=json.loads(self.parse_url(self.get_music_url.format(quote(keyword))))
#         music_list=music_dirt['data']['lists']
#         song_list=[]
#         for music in music_list:
#             song_name=music['FileName'].replace("<\\/em>", "").replace("<em>", "")
#             song_list.append({'hash':music['FileHash'], 'song_name':song_name})
#             print(str(len(song_list))+'---'+song_name)
#         return song_list
#
#     def download(self,song):
#         song_dirt=json.loads(self.parse_url(self.get_song_url.format(song['hash'])))
#         download_url=song_dirt['data']['play_url']
#         if download_url:
#             try:
#                 # 根据音乐url地址，用urllib.request.retrieve直接将远程数据下载到本地
#                 urllib.request.urlretrieve(download_url, 'd:/music/' + song['song_name'] + '.mp3')
#                 print('Successfully Download:' + song['song_name'] + '.mp3')
#             except:
#                 print('Download wrong~')
#
# if __name__ == '__main__':
#     kugou=KuGou()
#     while True:
# 	    keyword=input('请输入要下载的歌曲名：')
# 	    print('-----------歌曲《'+keyword+'》的版本列表------------')
# 	    music_list=kugou.get_music_list(keyword)
# 	    song_num=input('请输入要下载的歌曲序号：')
# 	    kugou.download(music_list[int(song_num)-1])

#encoding=utf-8
"""
@File    :  kugou.py
@Author  :  heram
@Time    :  2019-07-15 16:25:47
"""

import re
import json
import time
import requests
import os

def search(song_name):
     """搜索歌曲"""
     search_url = "https://songsearch.kugou.com/song_search_v2?callback=jQuery112405132987859127838_{}&page" \
                  "=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_fil" \
                  "ter=0&_={}&keyword={}".format(str(int(time.time()*1000)), str(int(time.time()*1000)), song_name)
     obj = requests.get(search_url)
     start = re.search("jQuery\d+_\d+\(?", obj.text)
     data = json.loads(obj.text.strip().lstrip(start.group()).rstrip(")"))
     return data['data']['lists']

def download(song_list, dir):
     """下载歌曲"""
     # 展示前十个搜索结果
     for i in range(10):
         print(str(i + 1) + " >>> " + str(song_list[i]['FileName']).replace('<em>', '').replace('</em>', ''))
     num = int(input("\n请输入您想要下载的歌曲序号："))
     print("请稍等，下载歌曲中...")
     time.sleep(1)
     file_hash = song_list[num - 1]['FileHash']
     url = "http://m.kugou.com/app/i/getSongInfo.php?cmd=playInfo&hash={}".format(file_hash)
     obj = requests.get(url)
     data = obj.json()  # json格式
     download_url = data['url']
     file_path = ''
     try:
         if download_url:
             file_name = str(song_list[num - 1]['FileName']).replace('<em>', '').replace('</em>', '')
             file_path = os.path.join(dir, ' - '.join(file_name.split(' - ')[::-1]) + ".mp3")
             with open(file_path, "wb")as fp:
                 fp.write(requests.get(download_url).content)
             print("歌曲已下载完成!")
         else:
             print("无此歌曲链接")
     except Exception as e:
         if os.path.exists(file_path):
             os.remove(file_path)
         print(e)

if __name__ == '__main__':
     # 下载歌曲存放目录
     dir = "D:\music"
     s = 'y'
     while s=='y':
         try:
             # 搜索歌曲
             song_list = search(input("请输入您想要搜索的歌曲名称："))
             # 下载歌曲
             download(song_list, dir)
         except Exception as e:
             print(e)
             pass
         s = input('继续按y，退出按n:')