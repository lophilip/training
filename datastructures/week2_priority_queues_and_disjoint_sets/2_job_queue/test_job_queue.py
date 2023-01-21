from job_queue import *

def test1():
    nworker=2
    jobs=[1,2,3,4,4]
    
    job=assign_jobs(nworker,jobs)
    
    print(job)
    
    assert job == [AssignedJob(worker=0, started_at=0), AssignedJob(worker=1, started_at=0), AssignedJob(worker=0, started_at=1), AssignedJob(worker=1, started_at=2), AssignedJob(worker=0, started_at=4)]
    
    
    
if __name__=='__main__':
    test1()
    