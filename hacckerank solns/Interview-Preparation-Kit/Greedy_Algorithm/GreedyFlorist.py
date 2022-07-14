#!/bin/python

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    cost = 0
    c.sort(reverse=True)
    t = 1
    j = 1
    for i in range(0,len(c)):
        cost = cost + c[i]*t
        if(j%k==0):
            t+=1
        j+=1 
    return cost            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = map(int, raw_input().rstrip().split())

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
