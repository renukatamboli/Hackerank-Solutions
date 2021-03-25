#!/bin/python

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    count = [0]*len(arr)
    for i in range(0,len(arr)):
        count[arr[i]] = count[arr[i]]+1
    maxcount = max(count)
    return count.index(maxcount)    


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
