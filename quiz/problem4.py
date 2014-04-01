def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    result = 1
    counter = 0
    while result <= x:
        counter += 1
        result *= b
    return counter-1
