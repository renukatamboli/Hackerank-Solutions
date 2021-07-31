# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(0,n):
    s = input()
    if(re.match(r'^[4-6]([0-9]){3}-?([0-9]){4}-?([0-9]){4}-?([0-9]){4}',s) and (len(s)==16 or len(s)==19)):
        s = s.replace("-","")
        if(re.search(r'([0-9])\1{3,}',s)):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")
            
        
