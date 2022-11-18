# Uses python3
def edit_distance(s, t):
    len_x=len(s)+1
    len_y=len(t)+1
    difference = [[0 for x in range(len(s)+1)] for y in range(len(t)+1)] 


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


            difference[y][x]=minimum
    
    
    
    #print_matrix(difference) #for debugging only


    total_difference=difference[len_y-1][len_x-1]
    return total_difference



def print_matrix(matrix):
    for row in matrix:
        print (row)
        
if __name__ == "__main__":
    print(edit_distance(input(), input()))
