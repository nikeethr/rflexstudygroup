#!/bin/python3

import sys
import math
import re

def almost_equal(x, y, t=1e-2):
    return abs(x - y) < t

def encrypted_str(s):
    s = re.sub(' ', '', s)
    l = len(s)
    c_ = math.sqrt(l)
    c = int(c_)

    if not almost_equal(c, c_):
        c += 1

    return ' '.join([s[i:l:c] for i in range(c)])

if __name__ == "__main__":
    s = input().strip()
    print(encrypted_str(s))
