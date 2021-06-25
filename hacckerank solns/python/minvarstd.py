import numpy
n,m = map(int,raw_input().split())
lst= []
for i in range(0,n):
    lst.append(map(int,raw_input().split()))
myarray = numpy.array(lst)
print(numpy.mean(myarray, axis = 1))  
print(numpy.var(myarray, axis = 0))
print(round(numpy.std(myarray),11))
