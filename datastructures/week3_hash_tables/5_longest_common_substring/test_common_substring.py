from common_substring import *

def test1():
    answer=solve('cool','toolbox')
    print (answer)
    
    answer2=longest_common_substring('cool','toolbox')    
    print(answer2)

    assert answer==answer2, 'test 1 fail'
    
if __name__=='__main__':
    test1()