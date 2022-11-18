import sys

def get_number_of_inversions_1(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here

    split_inversion=0

    array_a=list(a[left:ave])
    array_b=list(a[ave:right])

    #assume that array_a and array_b is sorted, because merge sort

    array_a.sort()
    array_b.sort()
    
    for index_b in range(0,len(array_b)):               #like merge sort 
        i=array_b[index_b]
        if i<array_a[-1]:
            for x in range (len(array_a)-1,-1,-1):
                if array_a[x]>i:
                    split_inversion+=1
                else:
                    break
            
            

            
    
    number_of_inversions+=split_inversion


    return number_of_inversions

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here

    split_inversion=0

    
    #b[left:right]=a[left:right]

    index_low=left
    index_high=ave

    merge=[]

    #because merge sort

    while index_low < ave and index_high<right:

        if b[index_low]<=b[index_high]:
            merge.append(b[index_low])
            index_low+=1
        else:
            merge.append(b[index_high])
            index_high+=1
            number_of_inversions+=ave-index_low
    
    need_sort=False
    while index_low < ave:
        merge.append(b[index_low])
        index_low+=1
        #number_of_inversions+=1
        #need_sort=True

    while index_high < right:
        merge.append(b[index_high])
        index_high+=1

    if need_sort:
        merge.sort()

    #modify b so it is sorted
    assert len(b[left:right])==len(merge),'should be some length'
    b[left:right]=merge

            
    
    number_of_inversions+=split_inversion


    return number_of_inversions

def naive_get_number_of_inversion(a, b=0, c=0, d=0):

    number_of_inversions=0
    for i in range (0,len(a)):
        for j in range (i+1,len(a)):

            if a[i]>a[j]:
                number_of_inversions+=1
    
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = list(a)
    print(get_number_of_inversions(a, b, 0, len(a)))
