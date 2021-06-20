#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter
from itertools import takewhile
def isValid(s):
    ct = Counter(s)
    count = []
    for values in ct.most_common():
        count.append(values[1])
    new_list = [w for w in set(s) if ct[w] == max(count,key=count.count)]
    if(len(new_list)==len(set(s))):
        return "YES"
    else:
        if(len(new_list)==len(set(s))-1):
            odd = list(set(s).difference(new_list))
            oddcount=0
            for i in odd:
                oddcount=oddcount+ct[i]
            if(oddcount-max(count,key=count.count)>1):
                return "NO"
            else:
                return "YES"
        else:
            return "NO"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
