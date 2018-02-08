# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:41:33 2018

@author: Administrator
"""

import requests
from bs4 import BeautifulSoup

import os

import random #随机数模块

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
    }
    print('headers.py connection Success!')
    return header #返回值为 header这个字典


parser = 'html.parser'
#cur_path = 'D:\\pics\\'

#header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

header = requests_headers()

TotalNames = []
    


def downloadPic(Url,num,cur_path): 

    cur_path = cur_path    
    if num < 2:
        url = Url
    else:
        url = Url[:-5] + '-' + str(num) + '.html'
    sets_page = requests.get(url, headers=header)
    soupdownloadpic = BeautifulSoup(sets_page.text, parser)
    pic_src = soupdownloadpic.find('div', 'srcPic').find('img')['src']
    print(pic_src)
    
    try:              
        f = open(cur_path + str(num) +'.jpg', 'wb')
        f.write(requests.get(pic_src, headers=header).content)
    except:
        pass
    finally:
        f.close()
        
    return print('downloadPic() is ok')

def sets_pics_load(URL):
    url = URL
    
    sets_page = requests.get(url, headers=header)
    soupsetspicsload = BeautifulSoup(sets_page.text, parser)
    sets_name = str(soupsetspicsload.find_all('h2'))[5:-13]
    sets_nums = int(soupsetspicsload.find(class_='pages').find_all('a')[-2].get_text())
       
    cur_path = 'D:\\pics\\' + sets_name + '\\'
    
    #header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
    if sets_name in TotalNames:
        print('######### Already have %s  ##########'%sets_name)
    else:
        TotalNames.append(sets_name)
        print(TotalNames)
        print('*****    ' + str(len(TotalNames)) + '    *****')
        
        if os.path.exists(cur_path):
           print('directory exist!')
        else:
           os.mkdir(cur_path)
                            
        i = 1    
        while i <= sets_nums:
            downloadPic(url, i, cur_path)
            i += 1
    
    return print('sets_pics_load() is ok')
    #print(main_page.text)


mainurl = 'http://www.mm2mm.com/'

def Begin(Beginrul):
    cur_url = Beginrul
    cur_page = requests.get(cur_url, headers=header)
    soupbegin = BeautifulSoup(cur_page.text, parser)
    
    preview_link_list = soupbegin.find(id='img-container').find_all('a', target='_blank')[1::2]
    
    for link in preview_link_list:
        link = link['href']
        newlink = mainurl + link
        
        sets_pics_load(newlink)
        
    return print('Begin() is ok')
        


main_page = requests.get(mainurl, headers=header)
soup = BeautifulSoup(main_page.text, parser)
links = soup.find(class_='tags-box').find_all('a')
print(links)
linkNums = len(links)
titles = 1
shortlinks = []

while titles <= linkNums:
    
    link = links[titles].get('href')
    startlink = mainurl + link[1:]
    shortlinks.append(startlink)
    print(shortlinks)
    print('$$$$    %s shortlinksNums!'%str(len(shortlinks)))
    Begin(startlink)
    print(str(titles) + 'Finished!')
    titles += 1
        
print(TotalNames)
print(str(len(TotalNames)) +'  @@@@@'+'All Finished!')
