import numpy
n = int(raw_input())
lst = []
for _ in range(0,n):
    lst.append(map(int,raw_input().split()))
a = numpy.array(lst)
lst = []
for _ in range(0,n):
    lst.append(map(int,raw_input().split()))
b = numpy.array(lst)
print numpy.dot(a, b)


    


