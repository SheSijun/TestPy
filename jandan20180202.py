# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from lxml import etree

urls = ['http://jandan.net/ooxx/page --{}'.format(str(i)) for i in range(0,20)]
path = 'D://pictures'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def get_photo(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    photo_urls = selector.xpath('//p/a[@class="view_img_link"]/@href')
    for photo_url in photo_urls:
        data = requests.get('http:' + photo_url, headers=headers)
        fp = open(path + photo_url[-10:], 'wb')
        fp.write(data.content)
        fp.close()
        
for url in urls:
    get_photo(url)