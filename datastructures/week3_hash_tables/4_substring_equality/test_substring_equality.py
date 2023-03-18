from substring_equality import *
import random
import time
import string

def test1_solver_hash_class():
    s='trololo'
    
    solver=solver_hash_class(s)
    
    
    assert (solver.ask(0,0,7)==True)    
    assert (solver.ask(2,4,2)==True)
    
    assert (solver.ask(2,4,3)==True)
    assert (solver.ask(3,5,1)==True)
    assert (solver.ask(1,3,2)==False)
    
def test2_solver_hash_class():    
    s='aaababaabab'
    solver=solver_hash_class(s)
    solver_base=Solver(s)
    
    test_case=[[0,0,1],
            [0,0,2],
            [0,0,3],
            [0,0,4],
            [0,0,5],
            [0,0,6],
            [0,0,7],
            [0,0,8],
            [0,0,9],
            [0,0,10],
            [0,0,11],
            [0,1,1],
            [0,1,2],
            [0,1,3],
            [0,1,4],
            [0,1,5],
            [0,1,6],
            [0,1,7],
            [0,1,8],
            [0,1,9],
            [0,1,10],
            [0,2,1],
            [0,2,2],
            [0,2,3],
            [0,2,4],
            [0,2,5],
            [0,2,6],
            [0,2,7],
            [0,2,8],
            [0,2,9],
            [0,3,1],
            [0,3,2],
            [0,3,3],
            [0,3,4],
            [0,3,5],
            [0,3,6],
            [0,3,7],
            [0,3,8],
            [0,4,1],
            [0,4,2],
            [0,4,3],
            [0,4,4],
            [0,4,5],
            [0,4,6],
            [0,4,7],
            [0,5,1],
            [0,5,2],
            [0,5,3],
            [0,5,4],
            [0,5,5],
            [0,5,6],
            [0,6,1],
            [0,6,2],
            [0,6,3],
            [0,6,4],
            [0,6,5],
            [0,7,1],
            [0,7,2],
            [0,7,3],
            [0,7,4],
            [0,8,1],
            [0,8,2],
            [0,8,3],
            [0,9,1],
            [0,9,2],
            [0,10,1],
            [1,0,1],
            [1,0,2],
            [1,0,3],
            [1,0,4],
            [1,0,5],
            [1,0,6],
            [1,0,7],
            [1,0,8],
            [1,0,9],
            [1,0,10],
            [1,1,1],
            [1,1,2],
            [1,1,3],
            [1,1,4],
            [1,1,5],
            [1,1,6],
            [1,1,7],
            [1,1,8],
            [1,1,9],
            [1,1,10],
            [1,2,1],
            [1,2,2],
            [1,2,3],
            [1,2,4],
            [1,2,5],
            [1,2,6],
            [1,2,7],
            [1,2,8],
            [1,2,9],
            [1,3,1],
            [1,3,2],
            [1,3,3],
            [1,3,4],
            [1,3,5],
            [1,3,6],
            [1,3,7],
            [1,3,8],
            [1,4,1],
            [1,4,2],
            [1,4,3],
            [1,4,4],
            [1,4,5],
            [1,4,6],
            [1,4,7],
            [1,5,1],
            [1,5,2],
            [1,5,3],
            [1,5,4],
            [1,5,5],
            [1,5,6],
            [1,6,1],
            [1,6,2],
            [1,6,3],
            [1,6,4],
            [1,6,5],
            [1,7,1],
            [1,7,2],
            [1,7,3],
            [1,7,4],
            [1,8,1],
            [1,8,2],
            [1,8,3],
            [1,9,1],
            [1,9,2],
            [1,10,1],
            [2,0,1],
            [2,0,2],
            [2,0,3],
            [2,0,4],
            [2,0,5],
            [2,0,6],
            [2,0,7],
            [2,0,8],
            [2,0,9],
            [2,1,1],
            [2,1,2],
            [2,1,3],
            [2,1,4],
            [2,1,5],
            [2,1,6],
            [2,1,7],
            [2,1,8],
            [2,1,9],
            [2,2,1],
            [2,2,2],
            [2,2,3],
            [2,2,4],
            [2,2,5],
            [2,2,6],
            [2,2,7],
            [2,2,8],
            [2,2,9],
            [2,3,1],
            [2,3,2],
            [2,3,3],
            [2,3,4],
            [2,3,5],
            [2,3,6],
            [2,3,7],
            [2,3,8],
            [2,4,1],
            [2,4,2],
            [2,4,3],
            [2,4,4],
            [2,4,5],
            [2,4,6],
            [2,4,7],
            [2,5,1],
            [2,5,2],
            [2,5,3],
            [2,5,4],
            [2,5,5],
            [2,5,6],
            [2,6,1],
            [2,6,2],
            [2,6,3],
            [2,6,4],
            [2,6,5],
            [2,7,1],
            [2,7,2],
            [2,7,3],
            [2,7,4],
            [2,8,1],
            [2,8,2],
            [2,8,3],
            [2,9,1],
            [2,9,2],
            [2,10,1],
            [3,0,1],
            [3,0,2],
            [3,0,3],
            [3,0,4],
            [3,0,5],
            [3,0,6],
            [3,0,7],
            [3,0,8],
            [3,1,1],
            [3,1,2],
            [3,1,3],
            [3,1,4],
            [3,1,5],
            [3,1,6],
            [3,1,7],
            [3,1,8],
            [3,2,1],
            [3,2,2],
            [3,2,3],
            [3,2,4],
            [3,2,5],
            [3,2,6],
            [3,2,7],
            [3,2,8],
            [3,3,1],
            [3,3,2],
            [3,3,3],
            [3,3,4],
            [3,3,5],
            [3,3,6],
            [3,3,7],
            [3,3,8],
            [3,4,1],
            [3,4,2],
            [3,4,3],
            [3,4,4],
            [3,4,5],
            [3,4,6],
            [3,4,7],
            [3,5,1],
            [3,5,2],
            [3,5,3],
            [3,5,4],
            [3,5,5],
            [3,5,6],
            [3,6,1],
            [3,6,2],
            [3,6,3],
            [3,6,4],
            [3,6,5],
            [3,7,1],
            [3,7,2],
            [3,7,3],
            [3,7,4],
            [3,8,1],
            [3,8,2],
            [3,8,3],
            [3,9,1],
            [3,9,2],
            [3,10,1],
            [4,0,1],
            [4,0,2],
            [4,0,3],
            [4,0,4],
            [4,0,5],
            [4,0,6],
            [4,0,7],
            [4,1,1],
            [4,1,2],
            [4,1,3],
            [4,1,4],
            [4,1,5],
            [4,1,6],
            [4,1,7],
            [4,2,1],
            [4,2,2],
            [4,2,3],
            [4,2,4],
            [4,2,5],
            [4,2,6],
            [4,2,7],
            [4,3,1],
            [4,3,2],
            [4,3,3],
            [4,3,4],
            [4,3,5],
            [4,3,6],
            [4,3,7],
            [4,4,1],
            [4,4,2],
            [4,4,3],
            [4,4,4],
            [4,4,5],
            [4,4,6],
            [4,4,7],
            [4,5,1],
            [4,5,2],
            [4,5,3],
            [4,5,4],
            [4,5,5],
            [4,5,6],
            [4,6,1],
            [4,6,2],
            [4,6,3],
            [4,6,4],
            [4,6,5],
            [4,7,1],
            [4,7,2],
            [4,7,3],
            [4,7,4],
            [4,8,1],
            [4,8,2],
            [4,8,3],
            [4,9,1],
            [4,9,2],
            [4,10,1],
            [5,0,1],
            [5,0,2],
            [5,0,3],
            [5,0,4],
            [5,0,5],
            [5,0,6],
            [5,1,1],
            [5,1,2],
            [5,1,3],
            [5,1,4],
            [5,1,5],
            [5,1,6],
            [5,2,1],
            [5,2,2],
            [5,2,3],
            [5,2,4],
            [5,2,5],
            [5,2,6],
            [5,3,1],
            [5,3,2],
            [5,3,3],
            [5,3,4],
            [5,3,5],
            [5,3,6],
            [5,4,1],
            [5,4,2],
            [5,4,3],
            [5,4,4],
            [5,4,5],
            [5,4,6],
            [5,5,1],
            [5,5,2],
            [5,5,3],
            [5,5,4],
            [5,5,5],
            [5,5,6],
            [5,6,1],
            [5,6,2],
            [5,6,3],
            [5,6,4],
            [5,6,5],
            [5,7,1],
            [5,7,2],
            [5,7,3],
            [5,7,4],
            [5,8,1],
            [5,8,2],
            [5,8,3],
            [5,9,1],
            [5,9,2],
            [5,10,1],
            [6,0,1],
            [6,0,2],
            [6,0,3],
            [6,0,4],
            [6,0,5],
            [6,1,1],
            [6,1,2],
            [6,1,3],
            [6,1,4],
            [6,1,5],
            [6,2,1],
            [6,2,2],
            [6,2,3],
            [6,2,4],
            [6,2,5],
            [6,3,1],
            [6,3,2],
            [6,3,3],
            [6,3,4],
            [6,3,5],
            [6,4,1],
            [6,4,2],
            [6,4,3],
            [6,4,4],
            [6,4,5],
            [6,5,1],
            [6,5,2],
            [6,5,3],
            [6,5,4],
            [6,5,5],
            [6,6,1],
            [6,6,2],
            [6,6,3]
    ]
    
    testcase_random=[]
    
    for i in range(1000000):
        a=random.randint(0,len(s)-1)
        b=random.randint(0,len(s)-1)
        
        if b>a:
            c=random.randint(1,len(s)-b)
        else:
            c=random.randint(1,len(s)-a)
        testcase_random.append([a,b,c])
    
    testcase_sequential=[]
    still_case=True
    a=0
    b=0
    c=0
    while still_case:        
        if b>=a:
            max_len=len(s)-b
        else:
            max_len=len(s)-a
        
        for c in range(1,max_len):
            testcase_sequential.append([a,b,c])
            
        if a >= len(s)-1:
            still_case=False
            
        b+=1
        
        if b>=len(s):
            a+=1
            b=0
        
        
    
    for x in test_case:
        a=x[0]
        b=x[1]
        l=x[2]
        
        if solver.ask(a,b,l)!=solver_base.ask(a,b,l):
            print('test2 fail x'+str(x))
            print(a,b,l)
            
        assert solver.ask(a,b,l)==solver_base.ask(a,b,l)
        
    for x in testcase_random:
        a=x[0]
        b=x[1]
        l=x[2]
        
        if solver.ask(a,b,l)!=solver_base.ask(a,b,l):
            print('test2_random fail x'+x.str())
            print(a,b,l)
            
        assert solver.ask(a,b,l)==solver_base.ask(a,b,l)
        
    for x in testcase_sequential:
        a=x[0]
        b=x[1]
        l=x[2]
        
        if solver.ask(a,b,l)!=solver_base.ask(a,b,l):
            print('test2_sequential fail x'+x.str())
            print(a,b,l)
            
        assert solver.ask(a,b,l)==solver_base.ask(a,b,l)

def test3_solver_hash_class(s='aaababaabab'):    
    
    solver=solver_hash_class(s)
    solver_base=Solver(s)
    
    
    
    testcase_random=[]
    
    for i in range(1000000):
        a=random.randint(0,len(s)-1)
        b=random.randint(0,len(s)-1)
        
        if b>a:
            c=random.randint(1,len(s)-b)
        else:
            c=random.randint(1,len(s)-a)
        testcase_random.append([a,b,c])
    
    testcase_sequential=[]
    still_case=True
    a=0
    b=0
    c=0
    while still_case:        
        if b>=a:
            max_len=len(s)-b
        else:
            max_len=len(s)-a
        
        for c in range(1,max_len):
            testcase_sequential.append([a,b,c])
            
        if a >= len(s)-1:
            still_case=False
            
        b+=1
        
        if b>=len(s):
            a+=1
            b=0
      
            
    for x in testcase_random:
        a=x[0]
        b=x[1]
        l=x[2]
        
        if solver.ask(a,b,l)!=solver_base.ask(a,b,l):
            print('test2_random fail x'+x.str())
            print(a,b,l)
            
        assert solver.ask(a,b,l)==solver_base.ask(a,b,l)
        
    for x in testcase_sequential:
        a=x[0]
        b=x[1]
        l=x[2]
        
        if solver.ask(a,b,l)!=solver_base.ask(a,b,l):
            print('test2_sequential fail x'+x.str())
            print(a,b,l)
            
        assert solver.ask(a,b,l)==solver_base.ask(a,b,l)
        
        
def time_test():
    
    s=''
    
    for i in range(100000):
        s+=random.choice(string.ascii_letters)
    
    print(s)
    solver=solver_hash_class(s)
    solver_base=Solver(s)
    
    
    
    num_test=1000000
    
    testcase_random=[]
    
    for i in range(num_test):
        a=random.randint(0,len(s)-1)
        b=random.randint(0,len(s)-1)
        
        if b>a:
            c=random.randint(1,len(s)-b)
        else:
            c=random.randint(1,len(s)-a)
        testcase_random.append([a,b,c])
    
         
    #test for naive solver
    naive_start=time.time()
    naivesolution=[0]*num_test
    for i in range(0,num_test):
        a=testcase_random[i][0]
        b=testcase_random[i][1]
        l=testcase_random[i][2]
                        
        naivesolution[i]=solver_base.ask(a,b,l)
            
    naive_time=time.time()-naive_start
    
    #test for hash solver
    hash_start=time.time()
    hashsolution=[0]*num_test
    for i in range(0,num_test):
        a=testcase_random[i][0]
        b=testcase_random[i][1]
        l=testcase_random[i][2]
                        
        hashsolution[i]=solver.ask(a,b,l)
    hash_time=time.time()-hash_start
    
    
    print ('naive solver time: '+str(naive_time))
    print ('hash solver time: '+str(hash_time))
    if naive_time>hash_time:
        print('hash solver is fast er')
    else:
        print('warning: hash solver is slower then navie solver')

    
if __name__=='__main__':
    test1_solver_hash_class()
    test2_solver_hash_class()    
    test3_solver_hash_class(s='aaabaaaba')
    time_test()
    
    print('test pass')
    
    