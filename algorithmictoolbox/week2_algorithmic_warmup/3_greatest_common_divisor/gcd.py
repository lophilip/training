# Uses python3
from re import A
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_euclian(a,b):
    if b <=0:
        return a
    else:
        aprime=a%b
        result=gcd_euclian(b,aprime)
        return result



if __name__ == "__main__":
    
    a, b = map(int, input().split())
    #b=1000000000
    #a=1000000000
    print(gcd_euclian(a, b))
