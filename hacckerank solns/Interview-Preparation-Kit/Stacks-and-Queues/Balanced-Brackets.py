#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    balance = []
    for i in range(0,len(s)):
        if(s[i]=="{" or s[i]=="[" or s[i]=="("):
            balance.append(s[i])
        else:
            if(s[i]=="}"):
                if(len(balance)!=0 and  balance[len(balance)-1]=="{"):
                    balance.pop()
                else:
                    return "NO"
            if(s[i]=="]"):
                if(len(balance)!=0 and balance[len(balance)-1]=="["):
                    balance.pop()
                else:
                    return "NO"
            if(s[i]==")"):
                if(len(balance)!=0 and balance[len(balance)-1]=="("):
                    balance.pop()
                else:
                    return "NO"
    if(len(balance)==0):
        return "YES"
    else:
        return "NO"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        s = raw_input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
