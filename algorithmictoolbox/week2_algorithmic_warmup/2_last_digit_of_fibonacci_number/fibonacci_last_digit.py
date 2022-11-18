# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_optimized(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        temp=previous
        previous=current%10
        current=(temp+current) %10

    return current 


if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    #n=2
    print(get_fibonacci_last_digit_optimized(n))
