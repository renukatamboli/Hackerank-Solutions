#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr.sort()
    mindiff = pow(10,9)
    min_array = []
    for i in range(0,len(arr)-k+1):
        if(arr[k+i-1]-arr[i]<mindiff):
            mindiff =  arr[k+i-1]-arr[i]
    return mindiff
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    k = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr_item = int(raw_input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
