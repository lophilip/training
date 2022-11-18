# Uses python3
import sys

def fast_count_segments_1(starts, ends, points):
    #cnt = [0] * len(points)
    cnt=[]

    hash={}
    
    for i in range(len(starts)):
        for number in range(starts[i],ends[i]+1):
            if number not in hash:
                hash[number]=1
            else:
                hash[number]+=1
    
    for i in range(0,len(points)):
        if points[i] in hash:
            cnt.append(hash[points[i]])
        else:
            cnt.append(0)

    return cnt

def fast_count_segments_2(starts, ends, points):

    points_sort=list(points)
    points_sort.sort()
    points_sort_index=0
    points_sort_inrange=True
    points_dict={}

    
    starts_sort=list(starts)
    starts_sort.sort()
    starts_sort_index=0
    starts_sort_inrange=True

    ends_sort=list(ends)
    ends_sort.sort()
    ends_sort_index=0
    ends_sort_inrange=True
    
    start_line=points_sort[0]    
    if start_line>starts_sort[0]:
        start_line=starts_sort[0]

    
    segments=0


    for i in range(start_line,points_sort[-1]+1):
        
        
        #this works, but causes slow downds
        #segments+=starts_sort.count(i)
        #segments-=ends.count(i-1)

        while starts_sort[starts_sort_index]==i and starts_sort_inrange:
            if starts_sort_index<len(starts_sort)-1:
                starts_sort_index+=1
            else:
                starts_sort_inrange=False
            segments+=1

        while ends_sort[ends_sort_index]==i-1 and ends_sort_inrange:
            if ends_sort_index<len(ends_sort)-1:
                ends_sort_index+=1
            else:
                ends_sort_inrange=False
            segments-=1

        assert segments >=0

        #if i in points_sort:   #this would cause potential slow dows
        #    points_dict[i]=segments
        #replace with below:
        while points_sort[points_sort_index]==i and points_sort_inrange:
            if points_sort_index<len(points_sort)-1:
                points_sort_index+=1
            else:
                points_sort_inrange=False
            points_dict[i]=segments


    return_segments=[]
    for i in points:
        assert i in points_dict
        return_segments.append(points_dict[i])
    

    return return_segments        

def fast_count_segments_3(starts, ends, points):

    points_sort=list(points)
    points_sort.sort()
    points_sort_index=0
    points_sort_inrange=True

    points_dict={}


    
    starts_sort=list(starts)
    starts_sort.sort()
    starts_sort_index=0
    starts_sort_inrange=True

    ends_sort=list(ends)
    ends_sort.sort()
    ends_sort_index=0
    ends_sort_inrange=True
    
    start_line=points_sort[0]    
    if start_line>starts_sort[0]:
        start_line=starts_sort[0]

    
    segments=0



    points_to_loop=[]
    points_to_loop.extend(starts_sort)
    for i in ends_sort:
        points_to_loop.append(i+1)
    points_to_loop.extend(points)

    points_to_loop.sort() #points of interest: start points, end points, actual points 

    #for i in range(start_line,points_sort[-1]+1): do not need to loop through all numbers much too slow
    for i in points_to_loop:    
        
        #this works, but causes slow downds
        #segments+=starts_sort.count(i)
        #segments-=ends.count(i-1)
        #replace with below
        while starts_sort[starts_sort_index]==i and starts_sort_inrange:
            if starts_sort_index<len(starts_sort)-1:
                starts_sort_index+=1
            else:
                starts_sort_inrange=False
            segments+=1

        while ends_sort[ends_sort_index]==i-1 and ends_sort_inrange:
            if ends_sort_index<len(ends_sort)-1:
                ends_sort_index+=1
            else:
                ends_sort_inrange=False
            segments-=1

        assert segments >=0

        #if i in points_sort:   #this would cause potential slow dows
        #    points_dict[i]=segments
        #replace with below:
        while points_sort[points_sort_index]==i and points_sort_inrange:
            if points_sort_index<len(points_sort)-1:
                points_sort_index+=1
            else:
                points_sort_inrange=False
            points_dict[i]=segments


    return_segments=[]
    for i in points:
        assert i in points_dict
        return_segments.append(points_dict[i])
    

    return return_segments            


def fast_count_segments(starts, ends, points):
    return fast_count_segments_3(starts,ends,points)




def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
