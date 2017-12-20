import urllib
import urllib2
import re

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent' : user_agent}



url = 'https://www.qiushibaike.com/'
try:
	request = urllib2.Request(url,headers=headers)
	response = urllib2.urlopen(request)
	
	content = response.read().decode('utf-8')
	#pattern = re.compile(r'<div class=article.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?<span class=stats-vote><i class=number>(.*?)</i>', re.S)
	
	#pattern = re.compile('<div.*?author clearfix>.*?<h2>(.*?)</h2>.*?content>.*?span>(.*?)</span>(.*?)number>(.*?)</i>.*?number>(.*?)</i>',re.S)
	
	pattern = re.compile(r'<div.*?author.*?<h2>(.*?)</h2>.*?<i class=number>(.*?)</i>',re.S)
	items = re.findall(pattern,content)
	
	for item in items:
		haveImg = re.search('img',item[2])
		#print(item[0],item[1],item[3],item[4])
		if not haveImg:
			print '0',item[0]
			print '1',item[1]
			
	
	# print response.read()
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
