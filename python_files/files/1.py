# -*- coding: utf-8 -*-  # 原因：Python默认是以ASCII作为编码方式的，如果在自己的Python源码中包含了中文（或者其他的语言，比如小日本的日语……），
# 此时即使你把自己编写的Python源文件以UTF-8格式保存了；但实际上，这依然是不行的。
import requests
from bs4 import BeautifulSoup  # 通过BeautifulSoup库能很好地解析Requests库请求的网页，
# 并把网页源代码解析成Soup文档，以便过滤提取数据（Soup文档按标准的缩进格式的结构输出为结构化的数据，为数据的过滤提取做好准备）
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4636.4 Safari/537.36'}
s = 'y'
while s=='y':
    url = input('请输入网址:')
    res = requests.get('{}'.format(url),headers=headers)
    # res = res.text  # 将网页反映码以网页源码输出
    # print(res)
    try:
        soup = BeautifulSoup(res.text,'html.parser')  # 支持的python标准库中的HTML解析器（lxml HTML、Lxml XML、html5lib）
        print(soup.prettify())
    except ConnectionError:
        print('拒绝连接。')
    s = input('是否继续(y/n):')
