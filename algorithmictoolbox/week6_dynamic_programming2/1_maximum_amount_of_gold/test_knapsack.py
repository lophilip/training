from knapsack import *


def test_optimal_weight_knapsack_nonrepetive():

    bag=10
    w=[1,4,8]
    max=optimal_weight_knapsack_nonrepetive(bag,w)

    print(max)

if __name__=='__main__':

    test_optimal_weight_knapsack_nonrepetive()
