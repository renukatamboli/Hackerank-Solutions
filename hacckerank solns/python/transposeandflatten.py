import numpy
n,m = map(int,raw_input().split())
lst = []
for _ in range(0,n):
    lst.append(map(int,raw_input().split()))
print(numpy.transpose(numpy.array(lst)))
print(numpy.array(lst).flatten())


