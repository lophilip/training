def binart_search_recurrsive(keys,query,low,high):
    
    if low==high or low>high:
        if keys[low]==query:
            return low
        else:
            return -1
    else:
        mid_index=int((low+high)/2)

        if keys[mid_index]==query:
            #return mid_index
            #search for lowest
            
            lowest=binart_search_recurrsive(keys,query,low,mid_index-1)

            if lowest >-1 and lowest<mid_index:
                return lowest
            else:
                return mid_index
                
        elif keys[mid_index]<query:
            return binart_search_recurrsive(keys,query,mid_index+1,high)
        elif keys[mid_index]>query:
            return binart_search_recurrsive(keys,query,low,mid_index-1)
        else:
            assert(True),'should not go here??'



def binary_search(keys, query):
    # write your code here
    found=binart_search_recurrsive(keys,query,0,len(keys)-1)
    return found



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
