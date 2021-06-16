import numpy
n,m = map(int,raw_input().split())
lst = []
for i in range(0,n):
    lst.append(map(int,raw_input().split()))
my_array = numpy.array(lst)
print(max(numpy.min(my_array, axis = 1)))
    
    


