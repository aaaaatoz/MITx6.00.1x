def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    resultstring = ""
    for index in range(min(len(s1),len(s2))):
        resultstring += s1[index]
        resultstring += s2[index]
    
    if len(s1) < len(s2):
        resultstring += s2[len(s1):]
    else:
        resultstring += s1[len(s2):]
        
    return resultstring
