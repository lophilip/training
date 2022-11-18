import car_fueling

def test1():
    distance=950
    tank=400
    station=[200,375,550,750]
    refills=car_fueling.compute_min_refills(distance,tank,station)

    assert (refills==2),'refills in test1 should be 2'
    print ('test1 pass')

def test2():
    distance=10
    tank=3
    station=[1,2,5,9]
    refills=car_fueling.compute_min_refills(distance,tank,station)

    assert (refills==-1),'refills in test2 should be -1'
    print ('test2 pass')

def test3():
    distance=500
    tank=200
    station=[100,200,300,400]
    refills=car_fueling.compute_min_refills(distance,tank,station)

    assert (refills==2),'refills in test3 should be 2'
    print ('test3 pass')
if __name__=='__main__':
    test1()
    test2()
    test3()
