#Uses python3

import sys


def len_common_sub(a, b):

    s=[]
    t=[]
    for i in a:
        s.append(str(i))
    for i in b:
        t.append(str(i))

    len_x=len(s)+1
    len_y=len(t)+1
    difference = [[0 for x in range(len(s)+1)] for y in range(len(t)+1)] 

    #no operation list
    nooperation=[]


    #fill in first row
    for x in range (0,len_x):
        difference[0][x]=x
    

    #fill in first column
    for y in range(0,len_y):
        difference[y][0]=y


    #fill in column my column
    for x in range(1,len_x):
        for y in range(1,len_y):
            insertion=difference[y][x-1]+1
            deletion=difference[y-1][x]+1
            substition=difference[y-1][x-1]+1

            minimum=min([insertion,deletion,substition])

            if s[x-1]==t[y-1]:     #no operation           
                minimum=substition-1
                nooperation.append([x,y])


            difference[y][x]=minimum
    
    maxcount=0
    for i in range(0,len(nooperation)):
        count=0
        currentx=-1
        currenty=-1
        for j in range (i,len(nooperation)):
            if nooperation[j][0] > currentx and nooperation[j][1] > currenty:
                count+=1
                currentx=nooperation[j][0]
                currenty=nooperation[j][1]
        if count>maxcount:
            maxcount=count
    return maxcount
    
    #print_matrix(difference) #for debugging only


    #total_difference=difference[len_y-1][len_x-1]
    #return total_difference
    #return 5

def lcs2(a, b):
    #write your code here
    return len_common_sub(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
