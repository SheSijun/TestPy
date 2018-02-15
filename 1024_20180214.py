# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import os

import json

import random 

import re

import sys





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

    
    header = {
        'Connection':head_connection[random.randrange(0,len(head_connection))],
        'Accept':head_accept[0],
        'Accept-Language':head_accept_language[random.randrange(0,len(head_accept_language))],
        'User-Agent':head_user_agent[random.randrange(0,len(head_user_agent))],
        'Referer':"http://x2.pix378.pw/pw/thread.php?fid=13",
    }
   
    return header 



header = requests_headers()

print(header)

url = 'https://www.nvshens.com/gallery/'
parser = 'html.parser'
cur_path = 'D:\\1024Pics\\'
pic_path = ''


TotalNames = []

try:
    with open('D:\\1024Pics\\1024data.json','r') as f:
        TotalNames = json.load(f)
except:
    pass



a_dict = {":":"_"," ":"_","\\":"_",}


def multiple_replace(text,adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)



def downloadPic(picname, picUrl): 


#    
    try:              
        f = open(pic_path + picname +'.jpg', 'wb')
        f.write(requests.get(picUrl, headers=header).content)
    except:
        pass
    finally:
        f.close()
        
    return print('downloadPic() is ok %s is downloaded!'%picname)


#apicurl = 'http://p.usxpic.com/imghost/upload/image/20180213/21310154720.jpg'
#downloadPic('test3',apicurl)

def APageLinks(apageUrl):
    cur_page = requests.get(apageUrl, headers=header)
    soup = BeautifulSoup(cur_page.text, parser)
    dirname = soup.find("title").get_text()
    indexNum = dirname.find('[')
    dirname = dirname[:indexNum]
    
    
    if dirname in TotalNames:
        return print("Already ### %s #### downloaded!"%dirname)
    else:
        TotalNames.append(dirname)
        TotalNamesNum = len(TotalNames)
        
        print("#########  %d #########"%TotalNamesNum)
        try:
            with open('D:\\1024Pics\\1024data.json','w') as f:
                json.dump(TotalNames, f)
                print("TotalNames[] Updated %s"%dirname)
        except:
            print("Failed!!!!!!")
    
   
    
        pic_path = cur_path + str(dirname) + '\\'
        if os.path.exists(pic_path):
            print("directory exist!")
      
        else:
            os.mkdir(pic_path)
        os.chdir(pic_path)
        
        preview_link_list = soup.find('div',"tpc_content", id="read_tpc").find_all('img')
        
    
        for link in preview_link_list:
            linkurl = link['src']
            linkname = linkurl[-9:-4]
            linkName = multiple_replace(linkname,a_dict)
            
            downloadPic(linkName, linkurl)
            
        os.chdir(cur_path)

#page = 'http://x2.pix378.pw/pw/htm_data/14/1802/1011585.html'
#APageLinks(page)

def PLinkPs(plinkp):
    cur_page = requests.get(plinkp, headers=header)
    soup = BeautifulSoup(cur_page.text, parser)
    Links = soup.find_all(style="text-align:left;padding-left:8px")
    PLinks = Links[6:-1]
    
    firstUrl = 'http://x2.pix378.pw/pw/htm_data/'
    
    for link in PLinks:
        newlink = str(link)
        a = newlink.find("htm_data") + len('htm_data')
        b = newlink.find(".html")
        newlink = newlink[a:b]
        newlink = firstUrl + newlink + '.html'
        print(newlink)
        APageLinks(newlink)
        
        
Pages = 'http://x2.pix378.pw/pw/thread.php?fid=14'
#PLinkPs(Pages)

i = 1

while i < 9:
    page = Pages + '&page=' + str(i)
    PLinkPs(page)
    i += 1
        
    

    
    
    