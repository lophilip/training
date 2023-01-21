import build_heap
import random



def check_if_heap(data):
    assert isinstance(data,list),'data should be list'
    assert all(isinstance(x,int) for x in data),'data should be all int'

    heap=True
    for i in range(0,len(data)):
        
        child1,child2=build_heap.findchildren(data,i)
        if child1 is not None:
            if child1>=0:
                if data[i]>data[child1]:
                    heap=False
        
        if child2 is not None:
            if child2>=0:        
                if data[i]>data[child2]:
                    heap=False
    
    if heap is False:
        print('heap is invalid')
        print(data)

    return heap




def test_build_heap():
    data=[5,4,3,2,1]    #for native
    data2=list(data)    #for optimized
    swap=build_heap.build_heap_native(data)
    #print (data)
    #print(swap)

    swap2=build_heap.build_heap(data2)

    #assert data2 == [1,2,3,5,4],'data is not heap'
    assert check_if_heap(data2) is True,'data is not a heap'

    
def test_build_heap2():
    data=[1,2,3,4,5]
    
    swap2=build_heap.build_heap(data)
    
    assert check_if_heap(data) is True,'data is not a heap'

def test_build_heap3():
    data=[1886, 493, 371, 987, 1924, 30, 1841, 1788, 1725]
    data2=list(data)
    
    swap=build_heap.build_heap(data)
    swap2=build_heap.build_heap_native(data2)
    
    assert check_if_heap(data) is True,'data is not a heap'

def test_build_heap_random():
    data=[]

    l=random.randint(5,10)

    for i in range(0,l):
        data.append(random.randint(0,2000))
    original_data=list(data)
    
    swap2=build_heap.build_heap(data)
    
    assert check_if_heap(data) is True,'data is not a heap'


if __name__=='__main__':
    test_build_heap()
    test_build_heap2()
    test_build_heap3()
    test_build_heap_random()
    print('tests passed')
