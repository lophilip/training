import random

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_1n(numbers):
    n = len(numbers)
    largest=-1
    senlarge=-1

    for x in numbers:
        if x>largest:
            
            senlarge=largest
            largest=x
        elif x>senlarge:
            senlarge=x
        
    
    if largest >=0 and senlarge >=0:
        return senlarge *largest
    else:
        return -1

        

    
def test_short():
    numbers=[2,3,40,5,60]
    result=max_pairwise_product(numbers)
    print(result) 

    result_1n=max_pairwise_product_1n(numbers)
    
    assert(result==result_1n),'max_pairwise_product_1n failed'
    print (numbers)

def test_long():

    numbers=[]
    for x in range (0,1000):
        numbers.append(random.randint(0,10000))


    result=max_pairwise_product(numbers)
    print(result) 

    result_1n=max_pairwise_product_1n(numbers)
    
    assert(result==result_1n),'max_pairwise_product_1n failed'
    print (numbers)
    

def test_bignum():
    numbers=[100000,90000]
    
    result=max_pairwise_product(numbers)
    print(result) 

    result_1n=max_pairwise_product_1n(numbers)
    
    assert(result==result_1n),'max_pairwise_product_1n failed'
    assert(result_1n==9000000000)
    print (numbers)


    



if __name__ == '__main__':

    test=False
    if test:
        test_short()
        test_long()
        test_bignum()

    else:
        input_n = int(input())
        input_numbers = [int(x) for x in input().split()]
        print(max_pairwise_product_1n(input_numbers))
