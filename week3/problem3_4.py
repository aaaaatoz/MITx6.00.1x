def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    leftstring = [ x for x in string.ascii_lowercase ]
    for char in lettersGuessed:
        leftstring.remove(char)
    return "".join(leftstring)
