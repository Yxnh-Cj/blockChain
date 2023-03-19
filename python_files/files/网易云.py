"""
目标：网易云音乐单张图片下载
"""
# # 1.确定url
# import requests
#
# url = "https://p1.music.126.net/TNZDRyQQfjnJdmwlJbYNvQ==/109951166203005139.jpg?imageView&quality=89"
# # # 使用用户代理
# headers_ = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 "
#                   "Safari/537.36 "
# }
# #
# # # 2.发送请求，获取响应对象
# response = requests.get(url, headers=headers_)
# # # 字节类型
# bytes_data = response.content
# # # 3.保存数据
# # # 快捷规范：ctrl+alt L
# with open("中国加油歌.jpg", "wb") as f:
#     f.write(bytes_data)
# import requests
#
# """ 目标：网易云非VIP歌曲下载 小技巧： 音频=>找.m4a """ # 1.确定url url =
# "https://m701.music.126.net/20210723214834/df99959f8488bd3d925e77f55e8684f2/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj
# /9879313779/25c1/4b6d/541f/982eec262010248b62170926b64eeec0.m4a" # 使用用户代理 headers_ = { "User-Agent": "Mozilla/5.0 (
# Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36" } # 2.发送请求
# response = requests.get(url, headers=headers_) # 获取字节数据 bytes_data = response.content # 3.保存歌曲 with open(
# "照亮黑夜的太阳.mp3",'wb') as f: f.write(bytes_data) import requests
#
# """ 目标：下载网易云的MV 视频找包小技巧 1.点击media 2.复制url去浏览器访问，验证是否是MV """ # 1.确定目标url url =
# "https://6fonnr1.cachenode.cn:37506/fseeca82d4.a.bdydns.com/1924164272/cloudmusic/obj/core/9902859061" \
# "/ecf24e7374ec1c64cf44e35e89c22bd5.mp4?wsSecret=17ee294c76c907715c562a34c654a28d&wsTime=1627047381&http_cdnfrom" \
# "=bdcloud&max_age=31104000&r=csLMxLOSlEBTC8LdFx2MzAZ5vxvlU2mip0JMw3pKvt5Ynwg5" \
# "%2FrygXV5lofIBDRuMqk4Rf5o0RqnaPdAkip2gA1N8fKX7zrDZIgcfEwsTQ6Do30I1HY3WuIGAFqtt3bZvYxwS3bEA9FheKcXNMukSBMKESVswPsrh7%2B5kPFvyYoIPsHoM5gUwXKrQU51PabrrENDjsjXdyvEfZn9XgGpJCw%3D%3D&MqD7sp=hpmbjI-Lws7JzcjPy8jMx87Kyc3Zl56Ml8Kdm4abkYygxsmdy8rOncbLmczHnMbJz8_Oxpybm5rHxsienc3NzsjIz8abx5nKnNmRkJuak4mTws3ZnJOMi5DCzNmGmZCPi8LIzNmLlpKakIqLws7JzcbJzMbMx87ZnJeanJTCzc3Ly8nIys7Hz9mNmo6Mj5vCzM_P2YycipabwpO4yMq4jYfPmc-Qxs2MsLnJrom02YaZj42Wws7Pzw~~&UYs5cp=hpmMlJaPws7ZhpmNmo6Wm8K-u4uosZS5vrW-r425ydK-vq3ZhpmLi8LMz9mGmZeQjIvCzc3N0c3LzNHKy9HOz8rZhpmLlpKaws7JzcjPy8jLz8zGy8c~&sent_http_cdn-ip=175.6.53.35&sent_http_access-control-allow-origin=*&sent_http_access-control-allow-credentials=true&sent_http_access-control-allow-headers=DNT%2CX-CustomHeader%2CKeep-Alive%2CUser-Agent%2CX-Requested-With%2CIf-Modified-Since%2CCache-Control%2CContent-Type%2CRange&sent_http_access-control-expose-headers=Content-Range%2C%20Last-Modified&sent_http_cdn-source=bdcloud&sent_http_cache=state&sent_http_access-control-allow-methods=GET%2CPOST%2COPTIONS&sent_http_cdn-user-ip=118.249.190.207 "
#
# # 使用用户代理
# headers_ = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 "
#                   "Safari/537.36 "
# }
# # 2.发送请求
# response = requests.get(url, headers=headers_)
# # 获取字节数据
# bytes_data = response.content
#
# # 3. 保存视频
# with open("照亮黑夜的太阳.mp4", 'wb') as f:
#     f.write(bytes_data)
