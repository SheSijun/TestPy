# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import os

url = 'http://www.mzitu.com/page/'
parser = 'html.parser'
cur_path = 'D:\\pictures'


header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#main_page = requests.get(url, headers = header)
#print(main_page.text)

preview_page_cnt = 2
for cur_num in range(1, int(preview_page_cnt)+1):
    cur_url = url + str(cur_num)
    cur_page = requests.get(cur_url, headers=header)
    
    soup = BeautifulSoup(cur_page.text, parser)
    
    preview_link_list = soup.find(id='pins').find_all('a', target='_blank')[1::2]
    
    for link in preview_link_list:
        dir_name = link.get_text().strip().replace('?', '')
        link = link['href']
        soup = BeautifulSoup(requests.get(link).text, parser)
        
        pic_cnt = soup.find('div', class_='pagenavi').find_all('a')[4].get_text()
        
        pic_path = cur_path + dir_name
        if os.path.exists(pic_path):
            print("directory exist!")
        else:
            os.mkdir(pic_path)
        os.chdir(pic_path)
        print('Downloading' + dir_name + '...')
        
        for pic_index in range(1, int(pic_cnt)+1):
            pic_link = link + '/' + str(pic_index)
            cur_page = requests.get(pic_link, headers=header)
            soup = BeautifulSoup(cur_page.text, parser)
            pic_src = soup.find('div', 'main-image').find('img')['src']
            
            pic_name = pic_src.split('/')[-1]
            
            f = open(pic_name, 'wb')
            f.write(requests.get(pic_src, headers=header).content)
            f.close()
        
        os.chdir(cur_path)
        
print('Finished')
            
#            print(pic_src)
        
    