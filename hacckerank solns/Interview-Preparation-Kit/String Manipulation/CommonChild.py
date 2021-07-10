#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    lst = [[0]*(len(s1)+1) for i in range(0,len(s2)+1)]
    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            if(s1[i]==s2[j]):
                lst[i+1][j+1] = lst[i][j]+1
            else:
                lst[i+1][j+1] = max(lst[i+1][j],lst[i][j+1])
    return(lst[len(s1)][len(s2)])
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
