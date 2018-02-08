# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import os

url = 'http://cdn2.snapgram.co/imgs/2018/02/02/1-29.png'
parser = 'html.parser'
cur_path = 'D:\\pics\\'

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


f = open(cur_path + 'test4.jpg', 'wb')
f.write(requests.get(url, headers=header).content)
f.close()