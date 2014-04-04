def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    bestShift = 0
    bestCorrectWordNumber = 0
    words = text.split()
    for shift in range(26):
        correctWordNumber = 0
        for word in words:
            if isWord(wordList, applyShift(word,shift)):
                correctWordNumber +=1
        if bestCorrectWordNumber < correctWordNumber:
            bestCorrectWordNumber, bestShift = correctWordNumber, shift
    return bestShift
