# from tkinter import *
from tkinter import filedialog, ttk, Tk, Menu
import tkinter as tk
import os
import re
import json
import time
import requests


# 打开文件夹
def opendir():
    # dir=os.path.dirname(fpath.get())
    dir = 'D:/music/'
    os.system('start ' + dir)


# 爬取
def crawing():
    name = song_name.get()

    def search(song_name):
        """搜索歌曲"""
        search_url = "https://songsearch.kugou.com/song_search_v2?callback=jQuery112405132987859127838_{}&page" \
                     "=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_fil" \
                     "ter=0&_={}&keyword={}".format(str(int(time.time() * 1000)), str(int(time.time() * 1000)),
                                                    song_name)
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
                if os.path.exists(dir) == False:
                    os.makedirs(dir)
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
        dir = "D:\music"
        s = 'y'
        while s == 'y':
            try:
                # 搜索歌曲
                song_list = search(name)
                # 下载歌曲
                download(song_list, dir)
            except Exception as e:
                print(e)
                pass
            s = input('继续按y，退出按n:')


mygui = Tk(className="酷狗音乐爬取")
mygui.geometry('800x800')
mymenu = Menu()
# fpath=tk.StringVar()
song_name = tk.StringVar()
# mymenu.add_command(label="open")
# mymenu.add_command(label="add")
# mymenu.add_command(label="delete")
# mygui.config(menu=mymenu)
# ttk.Button(mygui,text='打开',command=getfile).grid(row=0,column=0)
# ttk.Entry(mygui,textvariable=fpath).grid(row=2,column=5)
tk.ttk.Button(mygui, text='open', command=opendir).grid(row=2, column=5)

# ttk.Button(mygui,text='open',command=main_search).grid(row=1,column=1)

tk.ttk.Entry(mygui, textvariable=song_name).grid(row=2, column=0)
btn = tk.Button(mygui, text='搜索并下载', command=crawing)
# btn['text']='搜索'
btn.grid()
tk.mainloop()
