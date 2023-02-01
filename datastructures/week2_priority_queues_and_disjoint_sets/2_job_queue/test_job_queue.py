from job_queue import *
import random
from time import time

def test1():
    nworker=2
    jobs=[1,2,3,4,4]
    
    job=assign_jobs_native(nworker,jobs)
    job_ot=assign_jobs(nworker,jobs)
    
    #print(job)
    #print(job_ot)
    
    assert job == [AssignedJob(worker=0, started_at=0), AssignedJob(worker=1, started_at=0), AssignedJob(worker=0, started_at=1), AssignedJob(worker=1, started_at=2), AssignedJob(worker=0, started_at=4)]
    assert job == job_ot
    
    print('test1 passed')





def test2():
    nworker=10
    jobs=[]
    
    for i in range(0,10000):
        jobs.append(random.randint(1,10))
        
    n1=time()
    job_nt=assign_jobs_native(nworker,jobs)
    n2=time()    
    native=n2-n1
    
    ot1=time()
    job_ot=assign_jobs(nworker,jobs)
    ot2=time()
    ot=ot2-ot1
    
    print('native: ',native)
    print('ot: ',ot)
    
    print('ot/native: ',ot/native)
    
    #assert ot/native < 0.2 ,'ot is more than 20% slower than native'
    
    #print (job_nt)
    #print (job_ot)
        
    assert len(job_nt) == len(job_ot)
    assert job_nt == job_ot
    
    for x in range(0,len(job_nt)):
        #assert job_nt[x].worker == job_ot[x].worker
        if job_nt[x].started_at != job_ot[x].started_at:
            print('x: ',x)
            print('job_nt[x].started_at: ',job_nt[x].started_at)
            print('job_ot[x].started_at: ',job_ot[x].started_at)
        assert job_nt[x].started_at == job_ot[x].started_at, 'job_nt[x].started_at != job_ot[x].started_at'
    
    print('test2 passed')    
    

def test3():
    nworker=4
    jobs=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    
    job_nt=assign_jobs_native(nworker,jobs)
    job_ot=assign_jobs(nworker,jobs)
    
    print(job_nt)
    print(job_ot)
    
    assert job_nt == job_ot,'job_nt != job_ot'
    
    """
    for x in range(0,len(job_nt)):        
        assert job_nt[x].started_at == job_ot[x].started_at
    """
    print('test3 passed')



def test_workerclass():
    workertype=workerclass(10)
        
    """
    workertype.extractmin()           
    for i in workertype.worker_heap:
        print (i.worker)
    print (workertype.worker_heap)
    
    
    workertype.extractmin()
    
    for i in workertype.worker_heap:
        print (i.worker)
    print (workertype.worker_heap)
    """
    
    for i in range(0,10):
        w=workertype.extractmin()
        print(w.worker)
        
if __name__=='__main__':
    #test1()
    #test2()
    test3()
    
    #test_workerclass()
    
    
    