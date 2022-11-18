from stack_with_max_naive import *



def test1():
    stack=StackWithMax()

    stack.Push(7)
    stack.Push(1)
    stack.Push(7)
    assert (stack.Max()==7)
    stack.Pop()
    assert (stack.Max()==7)

    print('test1 pass')


if __name__=='__main__':
    test1()
