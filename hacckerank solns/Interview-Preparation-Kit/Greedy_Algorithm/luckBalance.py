#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    luck = 0
    contests.sort(key=lambda contests:contests[0],reverse=True)
    for i in range(0,len(contests)):
        if(contests[i][1]==1):
            if(k==0):
                luck = luck -contests[i][0]
            else:
                k=k-1
                luck = luck + contests[i][0]
        else:
            luck = luck + contests[i][0]           
    return luck
            
            
            
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in xrange(n):
        contests.append(map(int, raw_input().rstrip().split()))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

