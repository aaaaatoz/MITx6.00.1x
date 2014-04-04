def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    text = getStoryString()
    wordList = loadWords()
    bestshift = findBestShift(wordList,text)
    return applyShift(text,bestshift) # Remove this comment when you code the function
