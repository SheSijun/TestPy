import urllib2

req = urllib2.Request('http://blog.csdn.net')
try:
	urllib2.urlopen(req)
except urllib2.HTTPError, e:
	if hasattr(e,"reason"):
		print e.code
		print e.reason
else:
	print "OK"
