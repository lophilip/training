from primitive_calculator import *


def test1():
    input=5

    native_sequence=greedy_optimal_sequence(input)

    print (native_sequence)

def debug_tree():
    node=optimal_sequence_tree(10)
    print(node)

    sequence=get_sequence_node(node)
    print (sequence)

def test2():
    sequence=optimal_sequence(5)

    assert sequence == [1,2,4,5]

    print ('test2 pass')

def test3():
    sequence=optimal_sequence(96234)
    #sequence=optimal_sequence(30)
    #answer1=[1,3,9,10,11,22,66,198,594,1782,5346,16038,16039,32078,96234]
    #answer2=[1,3,9,10,11,33,99,297,891,2673,8019,16038,16039,48117,96234]
    assert len(sequence) == 15
    
    valid=False
    for i in range(0,len(sequence)-1):
        first=sequence[i]
        next=sequence[i+1]

        
        assert(first+1 == next or first*2==next or first*3==next)
        



    print ('test3 pass')


if __name__=='__main__':

    #test1()

    #debug_tree()
    #test2()
    test3()






