import fractional_knapsack

def test_fractional_knapsack_sample1():
    capacity=50
    weights=[20,50,30]
    value=[60,100,120]
    value=fractional_knapsack.get_optimal_value(capacity,weights,value)

    assert (value==180.0),'value should be 180'

def test_fractional_knapsack_sample2():
    capacity=10
    weights=[30]
    value=[500]
    value=fractional_knapsack.get_optimal_value(capacity,weights,value)

    assert (value>=166.66 and value<=166.67),'value should be 166.667'


def test_fractional_knapsack_sample3():
    capacity=1000
    weights=[30]
    value=[500]
    value=fractional_knapsack.get_optimal_value(capacity,weights,value)

    assert (value==500)
if __name__=='__main__':
    test_fractional_knapsack_sample1()
    test_fractional_knapsack_sample2()
    test_fractional_knapsack_sample3()
    print("tests passed")
    