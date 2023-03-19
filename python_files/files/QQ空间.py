#!/usr/bin/env
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
info = input('输入QQ号:')
res = requests.get(f"https://user.qzone.qq.com/{info}/infocenter/?_t_=0.6244913654137765")
soup = BeautifulSoup(res.text,'lxml')
response = soup.prettify()
res = re.findall('<.*>',response)
print(res)
