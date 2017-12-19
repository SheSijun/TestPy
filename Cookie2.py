import cookielib
import urllib2

# Set the file to save the cookie, cookie.txt under the sibling directory
filename = 'cookie.txt'

# Declare a Mozillacookiejar object instance to save the cookie and write to the file
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open("http://www.baidu.com")

cookie.save(ignore_discard=True,ignore_expires=True)
