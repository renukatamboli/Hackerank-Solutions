# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
lst =  map(lambda x: x.group(),re.finditer(r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU\b])',raw_input()))
if(lst):
    for i in lst:
        print(i)
else:
    print(-1)
        
