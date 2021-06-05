#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
import collections
def makeAnagram(a, b):
    # Write your code here
    c = collections.Counter(a)
    d = collections.Counter(b)
    common = c & d
    return len(a)+len(b)-2*sum(common.values())         
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
