def fibonacci(n):
    y=[0,1,1]
    if(n<=2):
        return y[n]
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n = int(input())
print(fibonacci(n))
