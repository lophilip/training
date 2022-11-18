from max_sliding_window import *
import random


def test1():
    a=[2,7,3,1,5,2,6,2]
    window_size=4

    native=max_sliding_window_naive(a,window_size)

    opt=max_sliding_window_optimal_2(a,window_size)

    assert opt == native
    
    #print(native)


def test_random():
    a=[]
    window_size=33333
    for i in range (0,100000):
        #a.append(random.randint(0,100))
        a.append(0)
    
    native=max_sliding_window_naive(a,window_size)

    opt=max_sliding_window_optimal_2(a,window_size)

    assert opt == native

    print ('test_random() pass')


if __name__=='__main__':
    test1()
    test_random()

