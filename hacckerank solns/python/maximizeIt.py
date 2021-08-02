# Enter your code here. Read input from STDIN. Print output to STDOUT 
from itertools import product

k,m = map(int,input().split())
def square(list):
    return map(lambda x: x ** 2, list)
lst = []
for i in range(0,k):
    l  = list(map(int,input().split()))
    l.pop(0)
    lst.append(list(square(l)))    
c = [p for p in product(*lst)]
modulo = 0
for i in c:
    if(sum(i)%m>modulo):
        modulo =sum(i)%m
print(modulo)
    
