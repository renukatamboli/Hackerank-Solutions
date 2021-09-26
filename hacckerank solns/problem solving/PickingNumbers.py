def pickingNumbers(a):
    s = sorted(set(a))
    maxsubArray = 0
    for i in range(0,len(s)-1):
        if(a.count(s[i])>maxsubArray):
            maxsubArray = a.count(s[i])
        if(abs(s[i]-s[i+1])==1):
            totalCount = a.count(s[i])+a.count(s[i+1])
            if(maxsubArray<totalCount):
                maxsubArray = totalCount
    if(maxsubArray==0):
        return len(a)
    else:
        return maxsubArray        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
