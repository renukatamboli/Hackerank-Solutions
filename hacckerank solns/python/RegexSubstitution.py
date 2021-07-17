# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(0,n):
    print(re.sub(r"(?<=\s)\|\|(?=\s)", "or",re.sub(r"(?<=\s)&&(?=\s)","and",input())))

