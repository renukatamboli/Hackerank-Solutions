import numpy
n,m = map(int,raw_input().split())
A = []
for i in range(0,n):
    A.append(map(int,raw_input().split())) 
B = []
for i in range(0,n):
    B.append(map(int,raw_input().split()))
print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(numpy.divide(A,B))
print(numpy.mod(A,B))
print(numpy.power(A,B))

