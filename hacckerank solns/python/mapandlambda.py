cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = lambda  x:0 if x==1 else 1 if x==2 else fib(x-1)+fib(x-2)
    return (list(map(fib, [x for x in range(1,n+1)])))
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
