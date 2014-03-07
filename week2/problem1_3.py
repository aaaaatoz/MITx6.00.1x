def is_ordered(string):
	if len(string) == 1 : return True
	for i in xrange(len(string)-1):
		if string[i] > string[i+1] : return False
	return True

	
startindex = 0
maxlen = 1
index = 0

while index+maxlen < len(s):
	while index+maxlen < len(s) and is_ordered(s[index:index+maxlen+1]) :	# found the substring ordered and longer than the previous substring
		startindex = index
		maxlen += 1
	index += 1

print "Longest substring in alphabetical order is: %s" %s[startindex:startindex+maxlen]
