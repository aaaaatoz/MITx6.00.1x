def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    for c in xrange( n/20+2):
        for b in xrange( (n-20*c)/9+2):
            for a in xrange ((n-20*c-9*b)/6 +2):
                if (6*a + 9*b + 20*c) == n :
                    return True
    return False
