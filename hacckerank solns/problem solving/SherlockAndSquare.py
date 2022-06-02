#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    count=0
    numInBetween1 = int(math.ceil(math.sqrt(a)))
    numInBetween2 = int(math.floor(math.sqrt(b)))
    for i in range(numInBetween1,numInBetween2+1,1):
        if(i*i>=a and i*i<=b):
            count+=1
    return count
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    for q_itr in xrange(q):
        first_multiple_input = raw_input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
