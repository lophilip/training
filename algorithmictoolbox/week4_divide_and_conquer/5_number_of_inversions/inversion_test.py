from inversions import *
import random
def test1():
    a=[2,3,9,2]

    b=list(a)

        
    inversion=get_number_of_inversions(a,b,0,len(a))    
    assert inversion==2

    naive=naive_get_number_of_inversion(a)
    assert inversion==naive

    
    print ('test1 pass')


def test2():
    a=[2,2,3,9]
    b=list(a)
    
        
    inversion=get_number_of_inversions(a,b,0,len(a))    
    
    naive=naive_get_number_of_inversion(a)
    assert inversion==naive

    
    print ('test2 pass')

def test3():
    a=[9, 4, 10, 5, 8, 6, 6, 10, 8, 7]
    #a=[3, 4, 1, 7, 7]
    b=list(a)
            
    inversion=get_number_of_inversions(a,b,0,len(a))    
    
    naive=naive_get_number_of_inversion(a)
    assert inversion==naive

    
    print ('test3 pass')

def test4():
    a=[9, 4]
    b=list(a)
 
        
    inversion=get_number_of_inversions(a,b,0,len(a))    
    
    naive=naive_get_number_of_inversion(a)
    assert inversion==naive

    
    print ('test4 pass')

def test_random():

    size=5

    for repeat in range (0,100000):
        a=[]
        b=[]
        for i in range(0,size):
            a.append(random.randint(1,10))
        b=list(a)
        
        inversion=get_number_of_inversions(a,b,0,len(a))    
        
        naive=naive_get_number_of_inversion(a)

        if inversion!=naive:
            print('test random fail a=')
            print(a)
        assert inversion==naive

    
    print ('testrandom pass')





if __name__=='__main__':
    test1()
    test2()
    test3()
    test4()
    test_random()