# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_hand_seq(n):
    seq=[]
    if n==0:
        seq.append(0)       
    for x in range(0,n):
        if x<=1:
            seq.append(x)
        else:
            number=seq[x-1]+seq[x-2]
            seq.append(number)
    
    return seq

def calc_fib_hand(n):
    
    seq=calc_fib_hand_seq(n)    
    return seq[-1]

def calc_fib_hand_withoutseq(n):
    number=0
    current=1
    previous=0

    if (n <= 1):
        return n
            
    for x in range(0,n-1):
        temp=previous
        previous=current
        current=(temp+current)
    
    return current

if __name__=='__main__':
    n = int(input())
    #n=10
    print(calc_fib_hand_withoutseq(n))

    """
    print ('fibonacci sequence to '+str(n))
    number=calc_fib_hand_seq(n)
    for x in number:
        print(x)
    """


