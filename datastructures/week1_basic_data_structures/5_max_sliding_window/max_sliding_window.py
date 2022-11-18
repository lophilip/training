# python3


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


def max_sliding_window_optimal(sequence, m):
    window = []
    
    maxw=-1   #max of window

    max_window=[] #max of all windows

    


    for i in range(0,m):
        appendv=sequence[i]
        window.append(appendv)
        if appendv > maxw:
            maxw=appendv
        
    max_window.append(maxw)
    
    for i in range(m,len(sequence)):
        appendv=sequence[i]

        popped=window.pop(0)        
        if popped != maxw:
            window.append(appendv)
            if appendv > maxw:
                maxw=appendv
        else:
            window.append(appendv)
            maxw=max(window)
        max_window.append(maxw)
        
    return max_window


def max_sliding_window_optimal_2(sequence, m):
    que=[]              #index of largest number in sequece
    answer=[]           #largest number in window

    for i in range (0,len(sequence)):
        if len(que) > 0 and i-que[0]==m:
            que.pop(0)
        
        while len(que) > 0 and sequence[i] > sequence[que[-1]]:
            que.pop()
        que.append(i)
        if i-m+1 >=0:
            answer.append(sequence[que[0]])
        
    return answer

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    #print(*max_sliding_window_naive(input_sequence, window_size))

    print(*max_sliding_window_optimal_2(input_sequence, window_size))
