# Uses python3
import sys
from typing import ByteString



def get_change_dynamic(m,coins=[1,3,4],dict_number_coins={}):
    
    if m==0:
        return 0

    if m in dict_number_coins:
        return dict_number_coins[m]

    best=-1

    for c in coins:
        if c <= m:
            nexttry = get_change_dynamic(m-c,coins,dict_number_coins)
        if (best<0 or best>nexttry+1):
            best=nexttry+1

    dict_number_coins[m]=best
    return best


    
    

    return m // 4


def get_change_recursive_naive(m,coins=[1,3,4]):
    if m==0:
        return 0

    best=-1

    for c in coins:
        if c <= m:
            nexttry = get_change_recursive_naive(m-c,coins)
        if (best<0 or best>nexttry+1):
            best=nexttry+1
    
    return best
    

def get_change(m):
    best = get_change_dynamic(m)
    return best




if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
