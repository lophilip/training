# Uses python3
from re import L
import sys
import random

def partition3_33(a, l, r):
    x = a[l]
    j = l
    m = r

    i = l
    while i <= m:
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        elif a[i] > x:
            a[i], a[m] = a[m], a[i]
            m -= 1
        else:
            i += 1
    return (j, m)


def partition3(a, l, r):            

    m=partition2(a,l,r)

    mlower=m

    for i in range(m,l-1,-1):
        if a[i]==a[m]:
            mlower=i
        else:
            break
    mupper=m
    for i in range(m,r+1):
        if a[i]==a[m]:
            mupper=i
        else:
            break

    return mlower,mupper

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)    
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);

def randomized_quick_sort_3way(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    ml,mh = partition3(a, l, r)    
    randomized_quick_sort_3way(a, l, ml - 1);
    randomized_quick_sort_3way(a, mh + 1, r);

def cheat(a):
    a.sort()

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort_3way(a, 0, n - 1)
    #cheat(a)
    for x in a:
        print(x, end=' ')
