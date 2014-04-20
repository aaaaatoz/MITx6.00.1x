def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here
    if not start.getBefore():
        return start
    else:
        return findFront(start.getBefore())
