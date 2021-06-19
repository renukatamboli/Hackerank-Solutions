import numpy
p = map(float,raw_input().split())
v = int(raw_input())
print(numpy.polyval(p, v))
