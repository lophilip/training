# python3
import math


def build_heap_native(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps



def findparent(data,index):
    assert isinstance(data,list),'data should be list'
    assert isinstance(index,int),'index should be int'
    assert index<len(data),'index exceed data size'

    parent=index/2 -1
    parent=math.ceil(parent)
    assert isinstance(parent,int),'parent should be int'
    return parent

def findchildren(data,index):
    assert isinstance(data,list),'data should be list'
    assert isinstance(index,int),'index should be int'
    assert index<len(data),'index exceed data size'

    index+=1

    left=-1
    right=-1
    
    left=2*index
    right=left+1

    if left>len(data): #left has exceed size of data
        left=None
    if right>len(data): #right has exceed size of data
        right=None
    
    if left is not None:
        left-=1
    
    if right is not None:
        right-=1
        
    return left, right

def swap(data,index1,index2):
    assert isinstance(data,list),'data should be list'
    assert isinstance(index1,int),'index should be int'
    assert isinstance(index2,int),'index should be int'
    assert index1<len(data),'index exceed data size'
    assert index2<len(data),'index exceed data size'

    temp=data[index1]

    data[index1]=data[index2]
    data[index2]=temp
    

def shiftdown(data,i,s):
    assert isinstance(s,list),'s is swap list, should be list'
    maxindex=i
    size=len(data)


    leftc,rightc=findchildren(data,i)

    if leftc is not None:
        if leftc < size and data[leftc] < data[maxindex] and leftc >= 0:
            maxindex=leftc

    if rightc is not None:
        if rightc < size and data[rightc] < data[maxindex] and rightc >= 0:
            maxindex=rightc

    if i is not maxindex:
        s.append((i,maxindex))
        swap(data,i,maxindex)
        shiftdown(data,maxindex,s)


def build_heap_ot2(data):
    size=len(data)
    s=[]

    for i in range (size//2-1,-1,-1):
        shiftdown(data,i,s)

    return s
    
def build_heap_ot1(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)-1,0,-1): #start from back of stack        
        parent=findparent(data,i)
        parentvalue=data[parent]
        cvalue=data[i]       
        child=i 
        while parentvalue > cvalue:
            swap(data,parent,child)
            swaps.append((parent,child))
            child=parent
            parent=findparent(data,child)
            if child<0 or parent<0:
                break
            parentvalue=data[parent]
            cvalue=data[child]        
    return swaps

def build_heap(data):
    s=build_heap_ot2(data)
    return s


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
