# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    
    # write your code here

    price_per_weight=[]
    for x in range(0,len(values)):
        p=values[x]/weights[x]
        price_per_weight.append(p)


    left_capacity=capacity
    loot = 0    
    
    while left_capacity > 0 and sum(weights)>0:
        max_value_index=-1
        max_value=-1
        for x in range(0,len(values)): #find most expensive item that is still available
            if price_per_weight[x]>max_value and weights[x]>0:
                max_value=price_per_weight[x]
                max_value_index=x
        
        #fill the loot bag
        if left_capacity>=weights[max_value_index]: #fill most expensive, and take all
            left_capacity-=weights[max_value_index]            
            loot+=values[max_value_index]
            weights[max_value_index]=0


        else:   #fill most expensive, take what you can
            what_is_taken=left_capacity
            left_capacity-=what_is_taken
            
            loot+=what_is_taken*(price_per_weight[max_value_index])

            #adjust total weight and value
            weights[max_value_index]-=what_is_taken
            values[max_value_index]=weights[max_value_index]*price_per_weight[max_value_index]
    return loot



            






if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
