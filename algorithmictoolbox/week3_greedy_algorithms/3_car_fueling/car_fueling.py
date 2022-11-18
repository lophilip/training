# python3
import sys
#from turtle import st


def compute_min_refills(distance, tank, stops):
    # write your code here

    travel_distance=0
    number_refill=0
    refill_index=-1
    refill_station=[]
    impossible=False
    
    stops.append(distance) #add last city as fueling station
    while travel_distance+tank<distance and impossible==False:
        #find the furest it can travel on tank
        for x in range (refill_index,len(stops)-1):
            if stops[x+1] - travel_distance > tank:
                if x > -1:
                    if refill_index==x: #repeating station means impossible
                        impossible=True
                    else:
                        refill_station.append(x)
                        travel_distance=stops[x]
                        refill_index=x

                    break
                else:
                    impossible=True
                    break


    #remove fueling at stop city
    if len(stops)-1 in refill_station:
        refill_station.remove(len(stops)-1)
    
    if len(refill_station)>0:        
        if stops[refill_station[-1]]+tank>=distance:
            number_refill=len(refill_station)
        else:
            number_refill=-1
    elif tank>=distance:
        number_refill=0
    else:
        number_refill=-1
                    
    return number_refill

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    #data = list(map(int, input().split()))
    #assert len(data)==3,' need 5 entries'
    #d=data[0]
    #m=data[1]
    #stops=data[3:]    
    print(compute_min_refills(d, m, stops))
