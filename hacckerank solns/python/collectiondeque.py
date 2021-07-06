# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n = int(input())
for i in range(0,n):
    op = input().split()
    if(op[0]=="append"):
        d.append(int(op[1]))
    if(op[0]=="appendleft"):
        d.appendleft(int(op[1]))
    if(op[0]=="pop"):
        d.pop()
    if(op[0]=="popleft"):
        d.popleft()
    if(op[0]=="extend"):
        d.extend(int(op[1]))
    if(op[0]=="extendleft"):
        d.extendleft(int(op[1]))
    if(op[0]=="remove"):
        d.remove(int(op[1]))
    if(op[0]=="reverse"):
        d.reverse()
    if(op[0]=="rotate"):
        d.rotate(int(op[1]))
for i in d:
    print(i,end=" ")
