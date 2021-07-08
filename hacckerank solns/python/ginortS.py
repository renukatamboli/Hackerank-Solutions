# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
upper = [c for c in s if c.isupper()]
upper.sort()
lower = [c for c in s if c.islower()]
lower.sort()
odddigit = [c for c in s if c.isdigit() and int(c)%2==1]
odddigit.sort()
evendigit = [c for c in s if c.isdigit() and int(c)%2==0]
evendigit.sort()
print(''.join(lower)+''.join(upper)+''.join(odddigit)+''.join(evendigit))
