#https://github.com/suzcube/lab10-swe-SK-KOF.git
# Partner 1: Katie Flanagan
# Partner 2: Suzanne Kerns

import math
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a,b):
    if a < b:
        return a
    elif b < a:
        return b
    else:
        return square_root(a*a + b*b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if b<0:
        raise ValueError
    return math.log(a,b)

def exp(a, b):
    return a**b

