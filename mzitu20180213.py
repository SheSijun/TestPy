# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import os

import json

import random #随机数模块

import re

def requests_headers():
    head_connection = ['Keep-Alive','close']
    head_accept = ['text/html,application/xhtml+xml,*/*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5','en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']

    #header 为随机产生一套由上边信息的header文件
    header = {
        'Connection':head_connection[random.randrange(0,len(head_connection))],
        'Accept':head_accept[0],
        'Accept-Language':head_accept_language[random.randrange(0,len(head_accept_language))],
        'User-Agent':head_user_agent[random.randrange(0,len(head_user_agent))],
        'Referer':"http://www.mzitu.com",
    }
   
    return header #返回值为 header这个字典



header = requests_headers()

print(header)

url = 'http://www.mzitu.com/page/'
parser = 'html.parser'
cur_path = 'D:\\pictures\\'


TotalNames = []

try:
    
    with open('D:\\pictures\\data.json','r') as f:
        TotalNames = json.load(f)
except:
    pass

#header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#main_page = requests.get(url, headers = header)
#print(main_page.text)
startPageNum = 1
preview_page_cnt = 9

a_dict = {":":"_"," ":"_","\\":"_",}

def multiple_replace(text,adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

for cur_num in range(startPageNum, int(preview_page_cnt)+1):
    cur_url = url + str(cur_num)
    cur_page = requests.get(cur_url, headers=header)
    
    soup = BeautifulSoup(cur_page.text, parser)
    
    preview_link_list = soup.find(id='pins').find_all('a', target='_blank')[1::2]
    
    for link in preview_link_list:
        dir_name = link.get_text().strip().replace('?', '')
        
        
        
        if dir_name in TotalNames:
            print('Already downloading %s !!!'%dir_name)
        else:
            dir_Name = multiple_replace(dir_name,a_dict)
            link = link['href']
            soup = BeautifulSoup(requests.get(link).text, parser)
            
            pic_cnt = soup.find('div', class_='pagenavi').find_all('a')[4].get_text()
            
            pic_path = cur_path + dir_Name
            if os.path.exists(pic_path):
                print("directory exist!")
                break
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
            TotalNames.append(dir_name)
            try:
                with open('D:\\pictures\\data.json','w') as f:
                    json.dump(TotalNames, f)
            except:
                pass

print('From page %s to page %s  ! '%(startPageNum,preview_page_cnt))
print('########' + str(len(TotalNames)) + '  SetsPictures have loaded!  ')   
print(TotalNames)


try:
    with open('D:\\pictures\\data.json','w') as f:
        json.dump(TotalNames, f)
except:
    pass
print('Finished')
            
#            print(pic_src)
        
    