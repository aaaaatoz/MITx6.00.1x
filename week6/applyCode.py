def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    resultList = []
    for letter in text:
        if letter in coder:
            resultList.append(coder[letter])
        else:
            resultList.append(letter)
    return "".join(resultList)
