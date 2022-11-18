# Uses python3
from email.mime import multipart
import sys

TEST=False

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def lcm_optimized(a, b):


    result=int(a*b/gcd_euclian(a,b))

    return result



def gcd_euclian(a,b):
    if b <=0:
        return a
    else:
        aprime=a%b
        result=gcd_euclian(b,aprime)
        return result

def test():
    assert (24==lcm_naive(6,8)),'multiple should be 24'
    assert (24==lcm_optimized(6,8)),'multiple should be 24'

    #assert (467970912861==lcm_naive(761457,614573)),'multiple should be 467970912861'
    assert (467970912861==lcm_optimized(761457,614573)),'multiple should be 467970912861'
    print('test pass')

if __name__ == '__main__':

    if TEST:
        test()
    else:
    
        a, b = map(int, input().split())
        print(lcm_optimized(a, b))

