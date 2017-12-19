import urllib2
import cookielib

# Declare a Cookiejar object instance to save cookies
cookie = cookielib.CookieJar()

# Use the Httpcookieprocessor object from the URLLIB2 library to create a cookie processor
handler = urllib2.HTTPCookieProcessor(cookie)

# Build opener by Handler
opener = urllib2.build_opener(handler)

response = opener.open('http://www.baidu.com')

for item in cookie:
	print 'Name = ' + item.name
	print 'Value = ' + item.value

