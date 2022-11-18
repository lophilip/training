from process_packages import *


def printresponses(responses):
    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


def test1():
    buffer = Buffer_2nd_trial(1)
    requests=[Request(0,1),Request(1,1)]

    response=process_requests(requests,buffer)

    
    printresponses (response)

def test2():
    buffer = Buffer_2nd_trial(1)
    requests=[Request(0,1),Request(0,1)]

    response=process_requests(requests,buffer)

    printresponses (response)

def test3():
    buffer = Buffer_2nd_trial(1)
    requests=[Request(0,1),Request(0,0)]

    response=process_requests(requests,buffer)

    printresponses (response)

def test4():
    buffer = Buffer_2nd_trial(1)
    requests=[Request(0,0),Request(0,0)]

    response=process_requests(requests,buffer)

    expected_response=[Response(False,0),Response(False,0)]

    assert response == expected_response


def debug1():
    buffer = Buffer_2nd_trial(1)
    requests=[Request(0,1),Request(1,1)]

    response=process_requests(requests,buffer)

    printresponses (response)

if __name__=='__main__':
    #test1()
    #test2()
    #test3()
    test4()


    #debug1()