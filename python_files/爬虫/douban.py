# from bs4 import BeautifulSoup
# import requests
# import json
#
# headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/96.0.4664.45 Safari/537.36',
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' }
#
# url_path = 'https://www.pexels.com/zh-cn/search/'
# word = input('请输入你要下载的图片:')
# url_tra = 'http://howtospeak.org:443/api/e2c?user_key=dfcacb6404295f9ed9e430f67b641a8e&notrans=0&text=' + word
# english_data = requests.get(url_tra,headers=headers)
# js_data = json.loads(english_data.text)
# content = js_data['english']
# url = url_path + word + '/'
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text,'lxml')
# imgs = soup.select('article > a > img')
# list = []
# for img in imgs:
#     photo = img.get('src')
#     list.append(photo)
#
# path = 'C://Users/86153/Desktop/photo/'
#
# for item in list:
#     data = requests.get(item,headers=headers)
#     fp = open(path+item.split('?')[0][-10:],'wb')
#     fp.write(data.content)
#     fp.close()
