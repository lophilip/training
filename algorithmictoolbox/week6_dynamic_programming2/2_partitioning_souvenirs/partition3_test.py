from partition3 import *
import random

def test1():
    a=[17,59,34,57,17,23,67,1,18,2,59]
    
    resultd=partition3_dynamic(a)
    resultb=partition3_brute(a)

    #print (resultd)
    assert resultd==resultb

def test2():
    a=[1,1,1]
    
    resultd=partition3_dynamic(a)
    resultb=partition3_brute(a)

    #print (resultd)
    assert resultd==resultb

def test3():
    a=[1,2,3,4,5,5,7,7,8,10,12,19,25]
    
    resultd=partition3_dynamic(a)
    resultb=partition3_brute(a)

    #print (resultd)
    assert resultd==resultb

def test_random():
    


    for repeat in range(0,200):
        a=[]
        for i in range(1,random.randint(0,20)):
            a.append(random.randint(1,100))


        
        resultd=partition3_dynamic(a)
        resultb=partition3_brute(a)

        if resultd!=resultb:
            print(a)

        #print (resultd)
        assert resultd==resultb


if __name__=='__main__':
    test1()
    test2()
    test3()
    print('test passed, now testing random')
    test_random()

