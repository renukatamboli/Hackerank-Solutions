#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
from calendar import timegm
 
def time_delta(t1, t2):
   fmt= '%a %d %b %Y %H:%M:%S %z'
   dt1 = timegm(datetime.strptime(t1, fmt).utctimetuple()) 
   dt2 = timegm(datetime.strptime(t2, fmt).utctimetuple()) 
   return str(int(abs(dt2-dt1)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
