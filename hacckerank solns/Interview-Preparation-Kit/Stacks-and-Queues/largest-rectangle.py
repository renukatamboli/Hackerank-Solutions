#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    longestArea = 0
    for i in range(0,len(h)):
        j=i
        k=i-1
        count=0
        while(j<len(h) and h[i]<=h[j]):
            count+=1
            j+=1
        while(k>=0 and h[k]>=h[i]):
            count+=1
            k-=1
        if(h[i]*count>longestArea):
            longestArea = h[i]*count
    return longestArea
                
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    h = map(int, raw_input().rstrip().split())

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
