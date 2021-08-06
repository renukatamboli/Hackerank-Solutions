#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
word = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in range(0,m):
    for j in range(0,n):
        word.append(matrix[j][i])
word = "".join(word)
word= re.sub(r'(?<=[a-zA-Z0-9])[\($!@#,%&\)\. ]{1,}(?=[a-zA-Z0-9])', r' ', word)
print(word)

