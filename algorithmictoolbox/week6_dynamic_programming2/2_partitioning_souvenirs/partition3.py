# Uses python3
import sys
import itertools


def partition3_dynamic(A):
    

    total=sum(A)

    if total % 3 !=0 or len(A)<3:
        return 0 #can not even divide into 3
    else:
        #create 3d matrix. y is weight items, x is backpack 1, z is backpack 2
        matrix=[]

        backpack_max=int(total/3)
        num_weights=len(A)

        #create 1st layer
        layer=[]
        for x in range(0,backpack_max+1):
            slice=[]
            for y in range(0, backpack_max+1):
                if x==0 and y==0:
                    slice.append(True)
                else:
                    slice.append(False)
            layer.append(slice)
        matrix.append(layer)

        #create next layers

        

        for w in range(1,num_weights+1):
            layer=[]
            for x in range(0,backpack_max+1):
                slice=[]
                for y in range(0, backpack_max+1):

                    #find the max of P[x,y,i]=P[x,y,i-1] U P[x-ai,y,i-1] U P[x,y-ai,i-1]

                    weight=A[w-1]
                    sliceappend=False

                    sliceappend|=matrix[w-1][x][y]
                    sliceappend|=matrix[w-1][x-weight][y]
                    sliceappend|=matrix[w-1][x][y-weight]
                    """
                    if x==0 and y ==0:
                        sliceappend=True
                    elif weight==y or weight==x:
                        sliceappend=True
                    elif weight <= x and weight <= y:
                        #take the value above
                        sliceappend|=matrix[w-1][x][y]
                    elif weight <= x and weight > y:
                        sliceappend|=matrix[w-1][x-weight][y]
                    elif weight > x and weight <= y:
                        sliceappend|=matrix[w-1][x][y-weight]
                    """
                    
                    slice.append(sliceappend)

                layer.append(slice)

            matrix.append(layer)


    result=matrix[w][x][y]

    returnvalue=0
    if result:
        returnvalue=1

    return returnvalue






def partition3_brute(A):
    iter=itertools.product(range(3), repeat=len(A))
    for c in iter:
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def partition3(A):
    return partition3_dynamic(A)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

