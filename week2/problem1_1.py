 # Paste your code into this box 
#s is pre-defined, if you want to do some test, please unhashed the below lines:
#s = 'this is a test line for the script'
#s = 'azcbobobegghakl'                 # you should get 5
#s = 'bwpahgmioxuekotpqii'             # you should get 8

vowelstuple = ('a','e','i','o','u')
 
numberOfVowels = 0
 
for char in s:
    if char in vowelstuple : numberOfVowels += 1
print "Number of vowels: %d" %numberOfVowels
