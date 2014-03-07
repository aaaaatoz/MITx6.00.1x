 # Paste your code into this box 
counter = 0
if len(s) >= 3:
    for index in range (len(s)-2):
        if s[index:index+3] == 'bob': counter +=1

print "Number of times bob occurs is: %d" %counter
