# !/user/bin/env python3
# -*- coding: utf-8 -*-
# Author:Euler
import requests
import re
import os  # 文件夹及文件的判别设置
import time  # 用于有道翻译JS逆向中生成随机数
import hashlib  # 用于反反爬有道，用来做js逆向
from lxml import etree  # xpath方法
import threading  # 准备引入多线程实现异步爬虫
from random import choice  # 用于免费代理IP的随机选取  # choice从列表中选取合适项结果用因素表示，choices将选取结果做成列表 详见line25


# 小说爬取函数
def novel(name_, m, n):
    # 加入代理IP
    """
    proxy = {
        # "http": "http://11.11.11.11.123"  # 乱写的，不一定是可用的代理IP
        "http": "http://183.247.199.111:30001"  # 乱写的，不一定是可用的代理IP
    }
    """
    global text
    with open('D:/学习/六星/爬虫班预习/5.IP代理/免费IP.txt', 'r') as f:
        p = f.read().strip().split('\n')  # 变量l不明确
    proxy = eval(choice(p))  # 拿到免费代理IP
    # print(proxy)

    # 加入请求头
    headers_ = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36 '
    }
    # name = input('输入书名:')  # 输入书名
    # 可以索引的url，笔趣阁网站
    url_raw = 'https://www.bige7.com/s?q={}'.format(name_)  # 书名相关网址
    # 请求网页
    response = requests.get(url_raw, headers=headers_, proxies=proxy)  # 请求网页
    # html化
    html = etree.HTML(response.content.decode())  # 将之HTML化
    # 通过xpath获取章节名
    text_name = html.xpath('//h4[@class="bookname"]/a/text()')  # 用xpath方法获取章节名
    # 循环获取对应的书的链接
    href = ''
    # 多个书中获取链接
    for k in range(len(text_name)):
        if name_ in text_name:
            href = html.xpath('//h4[@class="bookname"]/a/@href')[text_name.index(name_)]
        else:
            if name_ in text_name[k]:
                href = html.xpath('//h4[@class="bookname"]/a/@href')[k]
    if href == '':
        return print('未搜索到该书！')
    # n = int(input('输入爬取章数:'))  # 获取爬取页数
    # 循环通过动态url获取从某起始章到某终结章
    for i in range(m, n + 1):
        # 循环获取动态url
        url = f'https://www.bige7.com{href}{i}.html'
        # 请求网页，获取网页源码
        res = requests.get(url, headers=headers_, proxies=proxy)
        # 解析网页
        str_data = res.content.decode()
        # 获取书名
        file_name = '《' + re.findall('<title>(.*?)</title>', str_data)[0][
                          :re.findall('<title>(.*?)</title>', str_data)[0].find('_')].replace(':', ',') + '》'
        # 如果不存在该书名文件夹则新建，否则略过，创建文件夹
        if not os.path.exists(file_name) and '最新' not in file_name and '页面不存' not in file_name:
            os.makedirs(file_name)

        try:
            # 获取每一章节名
            title = re.findall('<span class="title">(.*?)</span>', str_data)[0]
            # 排除符号干扰，排除符号干扰，title已经在第一次符号过滤时发生改变
            for j in title:
                if j == '：' or j == '_' or j == '?':
                    title = title[:title.find(j)]
                    break
                # 获取该章节内容
                # 获取内容
                text = re.findall('<div id="chaptercontent" class="Readarea ReadAjax_content">(.*)', str_data)[
                    0].replace(
                    '<br />', '\n')
        except IndexError:
            # latest_chapter
            # 获取最新章节名
            url_ = f'https://www.bige7.com{href}'
            # print(url_)
            # 获取网页源码
            res_ = requests.get(url_, headers=headers_, proxies=proxy).content.decode()
            html_ = etree.HTML(res_)
            latest_chapter = html_.xpath('//span[@class="last"]/a/text()')[0]
            print(f'最新章节为:{latest_chapter}')
            break
        # 存入对应文件夹
        with open(f'{file_name}/{title}.txt', 'w+', encoding='utf-8') as f:
            f.write(text)
            print(title + '------------下载成功!')


def idm(name_, d_):
    # 在下载的章节数大于等于15时启动多线程
    if len(name_) == 1 and (int(d_[name_[0]][1]) - int(d_[name_[0]][0]) + 1) >= 20:
        length = int(d_[name_[0]][1]) - int(d_[name_[0]][0]) + 1
        temp = int(d_[name_[0]][1])
        # l = int(input('输入次数:'))
        # 至少分20个多线程，每个线程启用一个代理IP，可以根据输入总章节数，每一章分一个线程
        r = 20
        # for k in range(9):
        #     name.append(name[0])
        # for i in range(len(name)):
        #     if i == 0:
        #         m = int(d[name[0]][0])
        #         n = m + length/len(name)
        #     else:
        #         m = int(d[name[0]][0]) + length/len(name)
        #         n = m + length/len(name)
        #     if n > length:
        #         n = length
        #     d[name[i]] = [m, n]
        for j in range(r):
            m = int(d_[name_[0]][0]) + (length / r) * j + j
            n = m + length / r
            if n > temp:
                n = temp
            s = threading.Thread(target=novel, args=(name_[0], int(m), int(n)))
            s.start()
    else:
        for j in name_:
            s = threading.Thread(target=novel, args=(j, int(d_[j][0]), int(d_[j][1])))
            s.start()


# 用于翻译，js逆向
def translation(word):
    lts = str(int(time.time() * 1000))
    salt = lts + '0'
    sign = hashlib.md5(('fanyideskweb' + word + salt + 'Ygy_4c=r#e#4EX^NUGUc5').encode()).hexdigest()
    # print(lts, salt, sign)
    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': lts,
        'bv': '03a6a27012b22bc3c7ecc76381772182',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    headers_ = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Safari/537.36',
        'Referer': 'https://fanyi.youdao.com/',
        # 'Cookie': 'OUTFOX_SEARCH_USER_ID=-561885679@10.108.162.139; OUTFOX_SEARCH_USER_ID_NCOO=2022937427.0624533; '
        #           'JSESSIONID=aaaOep_fEfXMZfZC0I08x; ___rl__test__cookies=1645855775774 '
    }
    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    res = requests.post(url, headers=headers_, data=data).content.decode()
    # print(res)
    result = re.search('"tgt":"(.*?)",', res).groups()[0]
    return result


# 主程序入口
if __name__ == '__main__':
    start_time = time.time()
    try:
        # 获取书名
        name = input('输入需要爬取的书名（用空格隔开）:').split(' ')
        # 定义空字典用于得到对应信息，并将之编成键值对
        d = {}
        # 添加字典内容
        for o in range(len(name)):
            d[name[o]] = input('输入%s爬取的起始章和终结章(用空格隔开):' % name[o]).strip().split(' ')
        # 用主循环多线程同时爬取多本小说内容
        idm(name, d)

    except Exception as e:
        print(translation(str(e)))
    finally:
        print('所用时间:{}'.format(time.time() - start_time))
        pass
