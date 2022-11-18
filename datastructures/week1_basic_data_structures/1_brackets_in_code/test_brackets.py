from check_brackets import *


def test1():


    result=find_mismatch('foo(bar[i)')

    assert result==10

def test2():
    text='[]'

    result=find_mismatch(text)

    assert result==-1

def test3():
    text=')'

    result=find_mismatch(text)

    assert result==1

def test4():
    text='[](()'

    result=find_mismatch(text)

    assert result==3

if __name__=='__main__':
    test1()
    test2()
    test3()
    test4()

    print('tests passed')


