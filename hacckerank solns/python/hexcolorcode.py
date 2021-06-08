# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(raw_input())
for i in range(0,n):
    str = re.split(r':| ',raw_input())
    for i in str:
        if(re.compile(r'^\#([A-F0-9a-f]{3}|[A-F0-9a-f]{6})\){0,1}[;,]$').match(i)):
            print(re.split(r';|,|\)',i)[0])
