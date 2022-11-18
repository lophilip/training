import sorting
import random

def test1():
    a=[2,3,9,2,2]
    a_original=list(a)

    a_original.sort()

    sorting.randomized_quick_sort(a,0,len(a)-1)

    assert a==a_original

    print('test1() pass')


def test_partition1():
    a=[2,3,9,2,2]

    m=sorting.partition2(a,0,len(a)-1)

    assert m == 2 

    m=sorting.partition2(a,0,len(a)-1)

    a=[2,3,9,2,2]
    ml,mh=sorting.partition3(a,0,len(a)-1)

    
    print('test_partition1() pass')


def test2():
    a=[2,3,9,2,2]

    a_original=list(a)

    sorting.randomized_quick_sort_3way(a,0,len(a)-1)

    a_original.sort()
    assert a_original==a

    print ('test2 pass')


def test3():
    a=[]

    a_original=list(a)

    sorting.randomized_quick_sort_3way(a,0,len(a)-1)

    a_original.sort()
    assert a_original==a

    print ('test3 pass')


def test4():
    a=[9,9,9,9,9,9,9,9,9,5,5,5,5,5,5,5,5,5,1,2,2,2,2,2,6,6,6,6,6,5,5,5,5,5,5,5,9]

    a_original=list(a)

    sorting.randomized_quick_sort_3way(a,0,len(a)-1)

    a_original.sort()
    assert a_original==a

    print ('test4 pass')


def test5():
    a=[100,2,2,2,2,2,2,2,2,9,9,9,9,9,9,9,9,9,9,9]

    a_original=list(a)

    sorting.randomized_quick_sort_3way(a,0,len(a)-1)

    a_original.sort()
    assert a_original==a

    print ('test5 pass')

def test_random():

    

    for i in range (0,10000): #test 1000 times
        a=[]
        size=random.randrange(0,1000)

        for j in range(0,size):
            number=random.randrange(0,50)

            for k in range(0,5):
                a.append(number)
            

    
        a_original=list(a)
        a_sort=list(a)
        a_sort.sort()

        sorting.randomized_quick_sort_3way(a,0,len(a)-1)

        

        if a!=a_sort:
            print('test randomize fail')
            print(a_original)

        assert a==a_sort



    print('test random pass')




if __name__=='__main__':
    test1()
    test_partition1()
    test2()
    test3()
    test4()
    test5()
    test_random()
