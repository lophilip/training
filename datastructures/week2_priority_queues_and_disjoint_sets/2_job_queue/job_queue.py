# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])



    

def assign_jobs_native(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result



class workertype():
    def __init__(self,worker,free_at):
        self.worker=worker
        self.free_at=free_at

class workerclass:
    def __init__(self,nworker):
        self.worker_heap=[]
        
        for i in range (0,nworker):
            #self.worker_heap.append(workertype(i,0))
            self.insert(workertype(i,0))
            
    def shiftdown(self,i):
        minindex=i                        
        
        l=2*i+1
        if l<len(self.worker_heap) and (self.worker_heap[l].free_at<self.worker_heap[minindex].free_at
                                        or (self.worker_heap[l].free_at==self.worker_heap[minindex].free_at and 
                                            self.worker_heap[l].worker<self.worker_heap[minindex].worker)) :
            minindex=l
            
        r=2*i+2
        if r<len(self.worker_heap) and (self.worker_heap[r].free_at<self.worker_heap[minindex].free_at
                                        or (self.worker_heap[r].free_at==self.worker_heap[minindex].free_at and
                                            self.worker_heap[r].worker<self.worker_heap[minindex].worker)) :
            minindex=r
        
        if i!=minindex:
            self.worker_heap[i],self.worker_heap[minindex]=self.worker_heap[minindex],self.worker_heap[i]
            self.shiftdown(minindex) 
    
    def shiftup(self,i):
        if i==0:
            return
        p=(i-1)//2
        if (self.worker_heap[p].free_at>self.worker_heap[i].free_at or 
                (self.worker_heap[p].free_at==self.worker_heap[i].free_at and 
                 self.worker_heap[p].worker>self.worker_heap[i].worker)):
            self.worker_heap[p],self.worker_heap[i]=self.worker_heap[i],self.worker_heap[p]
            self.shiftup(p)
            
    def insert(self,i):
        self.worker_heap.append(i)
        self.shiftup(len(self.worker_heap)-1)
        
    def extractmin(self):
        result=self.worker_heap[0]
        self.worker_heap[0]=self.worker_heap[len(self.worker_heap)-1]        
        self.worker_heap.pop()
        self.shiftdown(0)
        return result
    
    def num_worker(self):
        return len(self.worker_heap)
    
    def free_at(self):
        if len(self.worker_heap)==0:
            return float('inf')
        return self.worker_heap[0].free_at

class workerclass2:
    #uses priority queue
    def __init__(self,nworker):
        self.worker_heap=[]
        
        for i in range (0,nworker):
            #self.worker_heap.append(workertype(i,0))
            self.insert(workertype(i,0))            
        
    def extractmin(self):
        result=self.worker_heap[0]
        self.worker_heap=self.worker_heap[1:]
        return result
    
    def insert(self,i):
        self.worker_heap.append(i)
        self.worker_heap.sort(key=lambda x: x.free_at)
        

    
    
def assign_jobs_ot1(n_workers, jobs):
    workers=workerclass(n_workers)
    result=[]
    for i in jobs:
        w=workers.extractmin()
        start_time=w.free_at
        w.free_at+=i
        workers.insert(w)
        result.append(AssignedJob(w.worker, start_time))
    return result



    
def assign_jobs_ot2(n_workers, jobs):
    workers=workerclass2(n_workers)
    result=[]
    for i in jobs:
        w=workers.extractmin()
        start_time=w.free_at
        w.free_at+=i
        workers.insert(w)
        result.append(AssignedJob(w.worker, start_time))
    return result

def assign_jobs_ot3(n_workers, jobs):
    worker1=workerclass(n_workers)
    worker2=workerclass(0)
    
    freeworker=worker1
    busyworker=worker2
    result=[]
    for i in jobs:
        
        if freeworker.free_at()>busyworker.free_at() and busyworker.num_worker()>0:
            freeworker,busyworker=busyworker,freeworker
            
        w=freeworker.extractmin()
        start_time=w.free_at
        w.free_at+=i
        busyworker.insert(w)
        result.append(AssignedJob(w.worker, start_time))
    return result


def assign_jobs(n_workers, jobs):
    #return assign_jobs_native(n_workers,jobs)
    return assign_jobs_ot1(n_workers,jobs)
    #return assign_jobs_ot3(n_workers,jobs)
    

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
