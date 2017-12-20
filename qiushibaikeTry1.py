import urllib
import urllib2
import re
import thread
import time


class QSBK():
	def __init__(self):
		self.pageIndex = 1	
		self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
		self.headers = {'User-Agent':self.user_agent}
		self.story = []
		self.enable = False

	def getpage(self,pageIndex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/'+str(pageIndex)
			request = urllib2.Request(url,headers=self.headers)
			response = urllib2.urlopen(request)
			pageCode = response.read().decode('utf-8')
			return pageCode
		except urllib2.URLError,e:
			if hasattr(e,'reason'):
				print(u'Failed....'),e.reason
				return None

	def getpageItem(self,pageIndex):
		pageCode = self.getpage(pageIndex)
		if not pageCode:
			print(u'Page Not responding...')
			return None
		partten = re.compile(r'<div class=article.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?<span class=stats-vote><i class=number>(.*?)</i>'
,re.S)
		items = re.findall(partten,pageCode)
		pageItem = []
		for item in items:
			pageItem.append([item[0].strip(),item[1].strip(),item[2].strip()])
		return pageItem

	def loadPage(self):
		if self.enable == True:
			if len(self.story)<2:
				pageStories = self.getpageItem(self.pageIndex)
				if pageStories:
					self.story.append(pageStories)
					self.pageIndex +=1


	def getOneStory(self,pageStories,page):
		for story in pageStories:
			self.loadPage()
			raw = raw_input()
			if raw =='Q':
				self.enable = False
				return
		print(u'Page%s\tAuthor:%s\tPoint of Praise:%s\nContent:%s')%(page,story[0],story[2],story[1])

	def start(self):
		print "Searching for embarrassing encyclopedia jokes,press Enter to show jokes,press Q to exit:"
		self.enable = True
		self.loadPage()
		nowpage = 0
		while self.enable:
			if len(self.story)>0:
				pageStories = self.story[0]
				nowpage +=1
				del self.story[0]
				self.getOneStory(pageStories,nowpage)

test = QSBK()
test.start()
