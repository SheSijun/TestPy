from bs4 import BeautifulSoup
import requests
import sys

class downloader(object):
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/30_30655/'
        self.names = []     # Store chapter name
        self.urls = []      # Store chapter links
        self.nums = 0       # Store the number of chapter

    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html,"lxml")
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]),"lxml")
        a = a_bf.find_all('a')
        self.nums = len(a[12:])
        # Eliminate unnecessary chapters and count the chapters
        for each in a[12:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html,"lxml")
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8, '\n\n')
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print("Begin loading:")
    for i in range(dl.nums):
        dl.writer(dl.names[i], 'upUP.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("Has been downloaded: %.2f%% " % float(100 * i/(dl.nums) ) + '\r')
        sys.stdout.flush()
    print("Finshed!")
