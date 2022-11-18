# python3

from collections import namedtuple
import re

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
        self.time=0
        self.buffersizetime={}

    def process(self, request):
        # write your code here
        #self.finish_time.append(request)

        starttime=request[0]
        timeprocess=request[1]
        dropped=False

        exit_loop=False
        while exit_loop==False:
            i=starttime   
            
            if timeprocess>0:
                if i not in self.buffersizetime:            
                    self.buffersizetime[i]=1
                else:
                    if self.buffersizetime[i]<self.size:
                        self.buffersizetime+=1
                    else:
                        dropped=True
            
            i+=1
            if i>=starttime+request[1]:
                exit_loop=True          #exit if time excedded

        if dropped==False:
            self.time+=request[1]    


        return Response(dropped, starttime)

class Buffer_2nd_trial:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        assert isinstance(request,Request)
        # write your code here
        #self.finish_time.append(request)

        #pop off finish que, that is lower then request time
        while len(self.finish_time)>0 and self.finish_time[0] <= request.arrived_at:
            self.finish_time.pop(0)

        add_packet=request.arrived_at+request.time_to_process

        #if finish que is empty of course packet can be processed
        if len(self.finish_time)==0:
            self.finish_time.append(add_packet)
            return Response(False, request.arrived_at)
        
        #if finish_time que is full, packet is dropped
        if len(self.finish_time) >=self.size:
            return Response(True,-1)

        add_packet=max(request.arrived_at+request.time_to_process, self.finish_time[-1]+request.time_to_process)

        self.finish_time.append(add_packet)

        return Response(False,self.finish_time[-1]-request.time_to_process)

        


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    #buffer = Buffer(buffer_size)
    buffer = Buffer_2nd_trial(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
