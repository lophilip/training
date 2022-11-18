# Uses python3
import sys

def get_change(m):
    #write your code here
    coin=[10,5,1]  #always from largest to smallest

    value=m
    number_coin=0
    purse_coin=[]

    while value>0:
        for x in coin:
            if x<=value:
                value-=x
                number_coin+=1
                purse_coin.append(x)
                break; #found the biggest coin to fit value, exit for loop

    

    return number_coin

if __name__ == '__main__':
    #m = int(sys.stdin.read())
    m=int(input())
    print(get_change(m))
