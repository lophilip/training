# Uses python3
from re import L
import sys


class class_pcalc:
    def __init__(self,data,layer):
        self.value=data
        self.layer=layer
        
        self.plusone=None
        self.x3=None
        self.x2=None
        self.head=None




def greedy_optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    sequence.reverse()
    return sequence

def optimal_sequence_tree(n):
    
    layer=0
    calc_value={}
    list_layer=[]

    pcalc=class_pcalc(1,layer)
    

    list_layer=[pcalc]
    
    while n not in calc_value and len(list_layer)>0:

        for i in list_layer:
            if i.value not in calc_value:
                calc_value[i.value]=i
            else:
                if calc_value[i.value].layer>i.layer:
                    calc_value[i.value].layer=i



        next_layer=[]
        while len(list_layer)>=1:    

            node=list_layer[0]
            

            #create next layer of tree
            if node.value+1 not in calc_value:
                node.plusone=class_pcalc(node.value+1,node.layer+1)
                node.plusone.head=node
                next_layer.append(node.plusone)
            
            if node.value*3 not in calc_value:    
                node.x3=class_pcalc(node.value*3,node.layer+1)
                node.x3.head=node
                next_layer.append(node.x3)
            
            if node.value*2 not in calc_value:    
                node.x2=class_pcalc(node.value*2,node.layer+1)
                node.x2.head=node
                next_layer.append(node.x2)
            

            del(list_layer[0])
        list_layer=next_layer
    
    if n in calc_value:
        return calc_value[n]
    else:
        return None

def get_sequence_node(node):

    sequence=[]
    n=node

    while n is not None:
        sequence.append(n.value)
        n=n.head

    

    sequence.reverse()
    return sequence



def optimal_sequence2(n):

    node=optimal_sequence_tree(n)

    sequence=get_sequence_node(node)


    return sequence
def optimal_sequence(n):
    """Optimal sequence from 1 to n.
    You are given a primitive calculator that can perform the following three
    operations with the current number x:
    * multiply x by 2
    * multiply x by 3
    * add 1 to x
    Your goal is given a positive integer n, find the minimum number of
    operations needed to obtain the number n starting from the number 1.
    Samples:
    >>> list(optimal_sequence(1))
    [1]
    >>> list(optimal_sequence(145))
    [1, 3, 9, 18, 36, 72, 144, 145]
    >>> list(optimal_sequence(14512))
    [1, 3, 9, 10, 11, 33, 66, 67, 201, 402, 403, 1209, 3627, 3628, 7256, 14512]
    """
    
    calc_count=[0]*(n+1) #stores min number of calculations to index number

    calc_count[1]=1

    for n in range(2,n+1):
        index_min=n-1 #plus 1
        min_hops=calc_count[index_min]
        if n%3==0: #divible by 3
            if calc_count[n//3]<min_hops:
                index_min=n//3
                min_hops=calc_count[index_min]
        
        if n%2==0: #divible by 2
            if calc_count[n//2]<min_hops:
                index_min=n//2
                min_hops=calc_count[index_min]

        min_hops+=1
        calc_count[n]=min_hops

    sequence=[n]
    next_index=n
    while sequence[-1]>1:

        currenthop=sequence[-1] #current number

        next_index-=1
        next_hop=calc_count[next_index]

        if currenthop % 3==0:
            if calc_count[currenthop//3]<next_hop:
                next_index=currenthop//3
                next_hop=calc_count[next_index]
        
        if currenthop % 2 ==0:
            if calc_count[currenthop//2]<next_hop:
                next_index=currenthop//2
                next_hop=calc_count[next_index]
        
        sequence.append(next_index)
    
    sequence.reverse()
    return sequence






if __name__=='__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
