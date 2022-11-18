# Uses python3
import sys

TEST=False

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def find_sequence(listn):
    assert isinstance(listn,list),'listn should be list of numbers'
    

    success=False
    sequence_length=0
    sequence=[]

    if len(listn)>=2:
        max_length=int(len(listn)/2)

        for check_len in range (2,max_length+1):
            list1=list(listn[0:check_len])
            list2=list(listn[check_len:check_len+len(list1)])

            if list1 == list2:
                success=True
                sequence_length=len(list1)
                sequence=list1

    return success,sequence_length,sequence



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


def get_fibonacci_optimized(n, m):
    if n <= 10:
        return get_fibonacci_huge_naive(n,m)
    else:

        success=False
        length=0
        sequence=[]
        for x in range (11,n,10):
            #try to find a sequence
            fib=calc_fib_hand_seq(x)

            listn=list(fib)

            for y in range(0,len(listn)):
                listn[y]=listn[y]%m

            success,length,sequence=find_sequence(listn)

            if success:
                break;

        if success:
            index=n%length

            value=sequence[index]
            return (value)
        else:
            return get_fibonacci_huge_naive(n,m)
    
def test():
    assert (161==get_fibonacci_huge_naive(239,1000))
    
    assert ((True,8,[0,1,1,2,0,2,2,1])==find_sequence([0,1,1,2,0,2,2,1,0,1,1,2,0,2,2,1]))
    assert ((False,0,[])==find_sequence([0,1,2]))
    assert ((True,2,[0,1])==find_sequence([0,1,0,1,0,1]))

    
    assert (161==get_fibonacci_optimized(239,1000))
    assert (151==get_fibonacci_optimized(2816213588, 239))
    assert (0==get_fibonacci_optimized(9999999999999, 2))
    print ('test pass')

if __name__ == '__main__':
    if TEST:
        test()
    else:
        #input = sys.stdin.read();
        n, m = map(int, input().split())
        print(get_fibonacci_huge_naive(n, m))
