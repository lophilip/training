# Uses python3
import sys


def optimal_weight_knapsack_nonrepetive(bag_weight,w):
    #matrix=[[0]*(bag_weight+1)]*(len(w)+1)
    matrix=[]
    row=len(w)+1
    column=bag_weight+1

    #init matrix to 0   #may not be necessary
    for i in range (0,row):
        matrix.append([])
        for j in range (0,column):
            matrix[i].append(0)

    #fill in matrix
    for i in range (1,row):
        for j in range (1,column):
            
            w1=0         
            if j>=w[i-1]:   
                if j!=w[i-1]:
                    #w1=matrix[i][j-1]
                    w1=w[i-1]
                    if j-w[i-1]>=0:
                        w1+=matrix[i-1][j-w[i-1]]
                else:
                    w1=w[i-1]
            
            w2=matrix[i-1][j]
            """
            w2=matrix[i-1][j]

            other_weight=j-w[i-1]
            if other_weight>=0 and (j-1)>=0:
                w2+=matrix[i-1][other_weight]
            """

            value=max(w1,w2)
            matrix[i][j]=value

    
    return matrix[row-1][column-1]



def optimal_weight(W, w):
    # write your code here
    result=optimal_weight_knapsack_nonrepetive(W,w)
    return result
    """
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result
    """

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight_knapsack_nonrepetive(W, w))
