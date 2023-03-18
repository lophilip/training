from hash_substring import *


def test1_rabinKarp():
    
    text='abacaba'
    pattern='aba'
    
    position=rabinKarp(text,pattern)
    
    #print (position)
    assert (position == [0,4]),'could not find position'
    
    
if __name__=='__main__':
    test1_rabinKarp()
    
    print('all tests passed')