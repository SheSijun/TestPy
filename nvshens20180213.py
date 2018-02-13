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
        'Referer':"https://www.nvshens.com",
    }
   
    return header #返回值为 header这个字典



header = requests_headers()

print(header)

url = 'https://www.nvshens.com/gallery/'
parser = 'html.parser'
cur_path = 'D:\\nvshensPics\\'
pic_path = ''


TotalNames = []

try:
    with open('D:\\nvshensPics\\nvshendata.json','r') as f:
        TotalNames = json.load(f)
except:
    pass

a_dict = {":":"_"," ":"_","\\":"_",}


def multiple_replace(text,adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

#def downloadPic(picName, picUrl):
#    
#    pic_path = cur_path + picName
#    if os.path.exists(pic_path):
#        print("directory exist!")
#        #break
#    else:
#        os.mkdir(pic_path)
#    os.chdir(pic_path)
#    
#    print('Downloading ---  ' + picName + ' --- ')
#    f = open(picName, 'wb')
#    f.write(requests.get(picUrl, headers=header).content)
#    f.close()

def downloadPic(picname, picUrl): 

#    cur_path = cur_path    
#    if num < 2:
#        url = Url
#    else:
#        url = Url[:-5] + '-' + str(num) + '.html'
#    sets_page = requests.get(url, headers=header)
#    soupdownloadpic = BeautifulSoup(sets_page.text, parser)
#    pic_src = soupdownloadpic.find('div', 'srcPic').find('img')['src']
#    print(pic_src)
    
#    pic_path = down_path
#    os.chdir(pic_path)
#    
    try:              
        f = open(pic_path + picname +'.jpg', 'wb')
        f.write(requests.get(picUrl, headers=header).content)
    except:
        pass
    finally:
        f.close()
        
    return print('downloadPic() is ok %s is downloaded!'%picname)

#picurl = 'https://t1.onvshen.com:85/gallery/25389/24872/s/0.jpg'    
#picname = '1'
#num = 3
#downloadPic(picname, picurl)

def findPicUrls(pageUrl):
    
#    downPath = pic_path
    cur_page = requests.get(pageUrl, headers=header)
    soup = BeautifulSoup(cur_page.text, parser)
    
    preview_link_list = soup.find(id='hgallery').find_all('img')
    
#    os.chdir(pic_path)
    for link in preview_link_list:
        linkurl = link['src']
        linkname = link['alt']
        linkName = multiple_replace(linkname,a_dict)
        
        downloadPic(linkName, linkurl)
        
#    os.chdir(cur_path)

#pageUrl = 'https://www.nvshens.com/g/24872/2.html'      
#findPicUrls(pageUrl)



def findSetsUrls(setsUrl):
    set_page = requests.get(setsUrl, headers=header)
    soup = BeautifulSoup(set_page.text, parser)
    dirname = soup.find('div', 'albumTitle').find('h1').get_text()
    Set_num = int(soup.find(id='pages').get_text()[-4])
    
    if dirname in TotalNames:
        return print("Already ### %s #### downloaded!"%dirname)
    else:
        TotalNames.append(dirname)
        TotalNamesNum = len(TotalNames)
        
        print("#########  %d #########"%TotalNamesNum)
        try:
            with open('D:\\nvshensPics\\nvshendata.json','w') as f:
                json.dump(TotalNames, f)
                print("TotalNames[] Updated %s"%dirname)
        except:
            print("Failed!!!!!!")
           
        
        dirName = multiple_replace(dirname, a_dict)
        
        pic_path = cur_path + str(dirName) + '\\'
        if os.path.exists(pic_path):
            print("directory exist!")
    #                break
        else:
            os.mkdir(pic_path)
        os.chdir(pic_path)
        
        i = 1
        while i <= Set_num :
            pageurl = setsUrl + str(i) + '.html'
            findPicUrls(pageurl)
            i += 1   
            
        os.chdir(cur_path)

#pageUrl = 'https://www.nvshens.com/g/24872/'        
#findSetsUrls(pageUrl)


mainurl = 'https://www.nvshens.com'
startpage = 'https://www.nvshens.com/gallery/'

def pageLinks(pagelinkUrl):
    pageLUrl = pagelinkUrl
    page = requests.get(pageLUrl, headers=header)
    soup = BeautifulSoup(page.text, parser)
    pLinks = soup.find_all(class_='galleryli_link')
    
    for link in pLinks:
        link = link['href']
        newlink = mainurl + link
        findSetsUrls(newlink)
    
#pageLinks(startpage)
        
pageNum = 2
while pageNum < 100:
    startPage = startpage + str(pageNum) + '.html'
    pageLinks(startPage)
    pageNum += 1
    