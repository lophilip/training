# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def getminmax(matrixmin,matrixmax,operation,x,y):
    assert len(operation)==len(matrixmin[0])-1
    assert x<len(matrixmin[0])
    assert y<len(matrixmin[0])
    assert x!=y

    assert x<=y

    possible=[]

    for i in range(x,y):
        a=matrixmin[x][i]
        am=matrixmax[x][i]
        b=matrixmin[i+1][y]
        bm=matrixmax[i+1][y]
        assert a is not None        #this can happen if matrix is not filled out in diagonal order
        assert b is not None
        
        calc=evalt(a,b,operation[i])
        possible.append(calc)
        
        #calc=evalt(a,bm,operation[i])
        #possible.append(calc)

        #calc=evalt(am,b,operation[i])
        #possible.append(calc)

        calc=evalt(am,bm,operation[i])
        possible.append(calc)

    returnvaluemin=min(possible)
    returnvaluemax=max(possible)

    matrixmin[x][y]=returnvaluemin
    matrixmax[x][y]=returnvaluemax

    return returnvaluemin,returnvaluemax




def get_maximum_value(dataset):
    #write your code here
    expression=str(dataset)
    number=[]
    operation=[]

    num=""
    for c in expression:        
        assert c.isdigit() or c=='+' or c=='-' or c=="*"
        if c.isdigit():
            num+=c
        else:
            number.append(int(num))
            num=""

            operation.append(c)
    assert num.isdigit() #ends on a number
    number.append(int(num))

    
    #init min and max matrix
    matrix_min=[]
    matrix_max=[]

    size=len(number)

    for x in range(0,size):
        matrix_min.append([])
        matrix_max.append([])
        for y in range(0,size):
            matrix_min[x].append(None)
            matrix_max[x].append(None)

    #init cross of matrix
    for i in range(0,size):
        matrix_min[i][i]=number[i]
        matrix_max[i][i]=number[i]

    #fill in min  and max of matrix
    for yoffset in range(1,size):
        for x in range(0,size):
            y=x+yoffset
            if x!=y and x<size and y<size:
                getminmax(matrix_min,matrix_max,operation,x,y)
                

    
    #find the max in matrix_max
    maxevual=matrix_max[0][size-1]
    """
    for x in range (0,size):
        for y in range(0,size):
            if matrix_max[x][y] is not None:
                if maxevual<matrix_max[x][y]:
                    maxevual=matrix_max[x][y]
    """


    
    return maxevual


if __name__ == "__main__":
    print(get_maximum_value(input()))
