# Uses python3
import sys


def count_element(a,num,left,right):
    count=0
    for i in range(left,right+1):
        if a[i]==num:
            count+=1
    return count
        

def get_majority_element(a, left, right):
    if left > right:
        return -1
    elif left==right:
        return a[right]
    elif left + 1 == right:
        return a[left]
    else:    
        
        mid = int((left+right)/2)

        lower=get_majority_element(a,left,mid)
        upper=get_majority_element(a,mid+1,right)
        
        if lower == upper: #agree on majority:
            return lower
        else: #majority not agree, need to count
            lower_count=count_element(a,lower,left,right)
            upper_count=count_element(a,upper,left,right)

            if upper_count>lower_count:
                return upper
            else:
                return lower

    return -1

def get_majority_element_check(a):
    majority=get_majority_element(a,0,len(a)-1)

    number=count_element(a,majority,0,len(a)-1)

    if number > int(len(a)/2):
        return majority
    else:
        return -1


def naive_majority(a):  #this is not really naive, this is hash table/ non-comparison sorting T(n)=O(n) This is much easier then to use divide and conquer
    majority=-1
    hash_table={}

    for i in a:
        if i not in hash_table:
            hash_table[i]=0
        hash_table[i]+=1
        
        if majority<=-1:
            majority=i
        elif hash_table[majority]<hash_table[i]:
            majority=i
    
    return majority

def naive_majority_check(a):


    majority=naive_majority(a)

    number=count_element(a,majority,0,len(a)-1)

    if number > int(len(a)/2):
        return majority
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element_check(a) != -1:
        print(1)
    else:
        print(0)
