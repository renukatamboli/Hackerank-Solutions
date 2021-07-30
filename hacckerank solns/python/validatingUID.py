# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(0,n):
    s = input()
    if(len(list(set(s)))==len(list(s)) and len(list(s))==10):
        if(re.match(r"[a-zA-Z0-9]*[A-Z][a-zA-Z0-9]*[A-Z][a-zA-Z0-9]*",s)):
            if(re.match(r"[a-zA-Z0-9]*[0-9][a-zA-Z0-9]*[0-9][a-zA-Z0-9]*[0-9][a-zA-Z0-9]*",s)):
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")
        
            
