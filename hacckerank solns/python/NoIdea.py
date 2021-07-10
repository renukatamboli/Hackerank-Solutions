# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
lst = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
happy = [x for x in lst if x in A]
unhappy = [x for x in lst if x in B]
print(len(happy) - len(unhappy))
