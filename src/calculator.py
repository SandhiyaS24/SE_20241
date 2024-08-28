# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def fact(n):
    if(n==1 or n == 0):
        return 1
    else:
        return n*fact(n-1)
