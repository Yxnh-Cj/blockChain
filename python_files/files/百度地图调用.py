import requests
import json
address = input('请输入地点:')
par = {'address':address,'key':'cb6492a25c1451adbeca73623251'}
url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak=Qk9nulzKvkYssHoPV9fyAEVQlqb3DkLn&output=json&coordtype=wgs84ll&location=31.225696,121.49884'
res = requests.get(url,par)
response = eval(res.text)
print(response['result']['location']['lng'],response['result']['location']['lat'])