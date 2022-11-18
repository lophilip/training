from lcs2 import *



def test_len_common_sub():

    a=[1,2,3]
    b=[3,2,1]

    len=len_common_sub(a,b)
    assert(len==1)

def test_len_common_sub2():

    a=[2,3,1,2,3]
    b=[1,2,3]

    len=len_common_sub(a,b)
    
    assert len==3

    len=len_common_sub(b,a)
    
    assert len==3

def test_len_common_sub3():

    a=[2,2,2,3]
    b=[2,3]

    len=len_common_sub(a,b)    
    assert len==2

    len=len_common_sub(b,a)    
    assert len==2

def test_len_common_sub4():

    a=[2]
    b=[2,2]

    len=len_common_sub(a,b)    
    assert len==1

    len=len_common_sub(b,a)    
    assert len==1

def test_len_common_sub5():

    a=[2,7,7,7,5]
    b=[2,7,7,5]

    len=len_common_sub(a,b)    
    assert len==4

    len=len_common_sub(b,a)    
    assert len==4

def test_len_common_sub6():

    a=[3,3,1]
    b=[1,3,3]

    len=len_common_sub(a,b)    
    assert len==2

    len=len_common_sub(b,a)    
    assert len==2

def test_len_common_sub7():

    a=[2,7,5,2]
    b=[2,5]

    len=len_common_sub(a,b)    
    assert len==2

    len=len_common_sub(b,a)    
    assert len==2


if __name__=='__main__':
    test_len_common_sub()
    test_len_common_sub2()
    test_len_common_sub3()
    test_len_common_sub4()
    test_len_common_sub5()
    test_len_common_sub6()
    test_len_common_sub7()
    print('tests passed')
