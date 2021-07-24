# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string =raw_input()
m = re.search(r'([A-Za-z0-9])\1',string)
if(m):
    print(m.group(0)[0])
else:
    print(-1)
