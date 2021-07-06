n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(0,m):
    op = input().split()
    if(op[0]=="pop"):
        s.pop()
    if(op[0]=="remove"):
        try:
            s.remove(int(op[1]))
        except KeyError:
            pass
    if(op[0]=="discard"):
        s.discard(int(op[1]))
print(sum(list(s)))
