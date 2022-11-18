import binary_search


def test_binary_search_1():
    keys=[1,5,8,12,13]
    query=[8,1,23,1,11]
    index=[2,0,-1,0,-1]

    for x in range(0,len(query)):
        answer=binary_search.binary_search(keys,query[x])

        if answer!=index[x]:
            print("error (x=%d) query=%d is not index=%d, instead respond with answer=%d"%(x,query[x],index[x],answer))
            assert False, 'answer is not correct'
    
    print ('test 1 pass')


def test_binary_search_duplicates():
    keys=[2,4,4,4,7,7,9]
    query=[9,4,5,2]
    index=[6,1,-1,0]

    for x in range(0,len(query)):
        answer=binary_search.binary_search(keys,query[x])

        if answer!=index[x]:
            print("error (x=%d) query=%d is not index=%d, instead respond with answer=%d"%(x,query[x],index[x],answer))
            assert False, 'answer is not correct'
    
    print ('test 2 pass')

def test_binary_search_duplicates_debug():
    keys=[2,4,4,4,7,7,9]
    query=[9,4,5,2]
    index=[6,1,-1,0]

    x=1
    if True:
        answer=binary_search.binary_search(keys,query[x])

        if answer!=index[x]:
            print("error (x=%d) query=%d is not index=%d, instead respond with answer=%d"%(x,query[x],index[x],answer))
            assert False, 'answer is not correct'
    
    print ('test 2 pass')
if __name__=='__main__':
    test_binary_search_1()
    #test_binary_search_duplicates_debug()
