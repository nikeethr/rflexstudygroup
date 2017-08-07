import math

def equalize_histogram(h):
    """
    (list) -> list

    Returns the equalized version of the input histogram.
    
    >>> equalize_histogram([0,0,0,0,0,0,2,3,4,3,0,0,0,0])
    """

    L = len(h)
    N = float(sum(h))

    if L == 0 or L == 1:
        return h

    h_n = [x/N for x in h]
    g = [math.floor((L-1) * sum(h_n[:x+1])) for x in range(L)]
    return g
