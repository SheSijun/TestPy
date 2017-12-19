# import RE Module
import re

# To compile a regular expression into a pattern object, 
# note that the r in front of hello means "native string"
pattern = re.compile(r'hello')

# Use Re.match to match the text,get the matching result,
# and return none when the match connot be matched
result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo CQC!')
result3 = re.match(pattern,'helo CQC!')
result4 = re.match(pattern,'hello CQC!')

if result1:
	print result1.group()
else:
	print '1 match failed!'
	
if result2:
	print result2.group()
else:
	print '2 match failed!'

if result3:
	print result3.group()
else:
	print '3 match failed!'

if result4:
	print result4.group()
else:
	print '4 match failed!'


