import re
import json
import time
import requests
import os


def search(song_name):
    """搜索歌曲"""
    search_url = "https://songsearch.kugou.com/song_search_v2?callback=jQuery112405132987859127838_{}&page" \
                 "=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_fil" \
                 "ter=0&_={}&keyword={}".format(str(int(time.time() * 1000)), str(int(time.time() * 1000)), song_name)
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
    # 下载歌曲存放目录
    dir = "D:\music"
    s = 'y'
    while s == 'y':
        try:
            # 搜索歌曲
            song_list = search(input("请输入您想要搜索的歌曲名称："))
            # 下载歌曲
            download(song_list, dir)
        except Exception as e:
            print(e)
            pass
        s = input('继续按y，退出按n:')
