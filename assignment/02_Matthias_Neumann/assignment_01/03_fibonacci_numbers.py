#!/usr/bin/python3

## Task 03 –  Fibonacci Numbers

if __name__ == "__main__":
    bound=int(input("Upper bound for the fibonacci numbers: "))
    fib_prev=1
    fib_curr=0
    comma=""
    while fib_curr < bound:
        print(comma,end="")
        print(fib_curr,end="")
        comma=", "
        fib_curr,fib_prev=fib_curr+fib_prev,fib_curr
        

