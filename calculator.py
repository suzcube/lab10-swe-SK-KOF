
import math
#https://github.com/suzcube/lab10-swe-SK-KOF.git
# Partner 1: Katie Flanagan
# Partner 2: Suzanne Kerns


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def log(a, b):
    if b<0:
        raise ValueError
    return math.log(a,b)

def exp(a, b):
    return a**b




