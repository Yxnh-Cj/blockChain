# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import requests
import random
# import json
from hashlib import md5

# Set your own appid/appkey.
appid = '20211121001005067'
appkey = 'vawTE5iujrrBtuNj6Hvz'


# For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
query = ''
print('输入quit退出,输入其他键继续.')
def translation():
    global query
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path
    query = input('请输入:')  # '早上好。\n吃了吗。'
    if ord(query[0]) in range(65, 91) or ord(query[0]) in range(97, 123):
        from_lang = 'en'  # 原语言
        to_lang = 'zh'  # 目标语言
    else:
        from_lang = 'zh'  # 原语言
        to_lang = 'en'  # 目标语言

    def trans(query):
        # Generate salt and sign
        def make_md5(s, encoding='utf-8'):
            return md5(s.encode(encoding)).hexdigest()

        salt = random.randint(32768, 65536)
        sign = make_md5(appid + query + str(salt) + appkey)

        # Build request
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

        # Send request
        r = requests.post(url, params=payload, headers=headers)
        result = r.json()
        # for i in range(query.strip().count('\n')+1):
        #     print('“'+result['trans_result'][i]['src']+'”'+':'+result['trans_result'][i]['dst'])
        return result['trans_result'][0]['dst']

    print(trans(query))
if __name__=='__main__':
    while query!='quit':
        translation()
# # Show response
# response=json.dumps(result, indent=4, ensure_ascii=False)
# print(response)
