import cookielib
import urllib2

# Creating a Mozillacookiejar instance Object
cookie = cookielib.MozillaCookieJar()

# Read cookie content from file to variable
cookie.load('cookie.txt',ignore_discard=True, ignore_expires=True)

# Create requested request
req = urllib2.Request("http://www.baidu.com")

# Use the Urllib2 Build_opener method to create a opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
