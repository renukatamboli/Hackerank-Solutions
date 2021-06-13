import numpy
n,m,p = map(int,raw_input().split())
lst1 = []
lst2 = []
for _ in range(0,n):
    lst1.append(map(int,raw_input().split()))
for _ in range(0,m):
    lst2.append(map(int,raw_input().split()))
print(numpy.concatenate((lst1, lst2), axis = 0))
    


