# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string = raw_input()
pattern = raw_input()
m = re.search(pattern,string)
i=0
if(m is None):
    print(-1,-1)
while(m):
     print(m.start()+i,m.end()-1+i)
     i=i+m.start()+1
     m = re.search(pattern,string[i:])
    
