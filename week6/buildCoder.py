def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    import string
    CodeDict = {}
    for index in range(len(string.ascii_lowercase)):
        CodeDict[string.ascii_lowercase[index]] = string.ascii_lowercase[(index+shift)%26]
    for index in range(len(string.ascii_uppercase)):
        CodeDict[string.ascii_uppercase[index]] = string.ascii_uppercase[(index+shift)%26]
    return CodeDict
