def fib(n):
    num1=0
    num2=1
    if n==1:
        return num1
    elif n==2:
        return num2
    else:
        return fib(n-1)+fib(n-2)
