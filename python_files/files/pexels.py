# from bs4 import BeautifulSoup
# import requests
# from lxml import etree
# from 翻译 import trans
# import cv
# import matplotlib
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4636.4 Safari/537.36',
#     'referer': 'https://www.pexels.com/'
# }
# url_path = 'https://www.pexels.com/search/'
# content = input('请输入你要搜索的内容:')
# url = url_path+trans(content).replace(' ','%20')+'/'
# wb_data = requests.get(url,headers=headers)
# soup = BeautifulSoup(wb_data.text,'html.parser')
# imgs = soup.select('article > a > img')
# list = []
# for img in imgs:
#     photo = img.get('src')
#     list.append(photo)
# print(list)
# path = 'C:/Users/86153/Desktop/photo/'
# for item in list:
#     data = requests.get(item,headers=headers)
#     fp = open(path+item.split('?')[0][-10:],'wb')
#     fp.write(data.content)
#     fp.close()


