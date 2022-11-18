from points_and_segments import *
import random


def test1():
    starts=[0,7]
    ends=[5,10]
    points=[1,6,11]


    count=fast_count_segments(starts, ends, points)
    naive_count=naive_count_segments(starts, ends, points)

    assert count==naive_count

    print('test1 pass')

def test2():
    starts=[-10]
    ends=[10]
    points=[-100,100,0]


    count=fast_count_segments(starts, ends, points)
    naive_count=naive_count_segments(starts, ends, points)

    assert count==naive_count

    print('test2 pass')



def test3():
    starts=[-5, 121, -16, -54, -15, 54, 79, 98, -69, 88, 153, -49, 116, -56, -66, -73, 16, 17, -46, -94, 149, 5, -2, -19, 53, 79, 92, -93, 64, 184, -77, -5, -28, -28, -78, -70, -23, 85, 34, 23]
    ends=[174, 147, 77, -3, 0, 147, 145, 168, 97, 175, 189, 7, 136, -3, 93, -65, 115, 152, 85, -18, 183, 191, 179, 175, 105, 135, 164, -9, 66, 198, 161, 113, 36, 43, 191, 1, 5, 143, 36, 35]
    points=[7, 4, -7, 2, 13, 9, 0, -7, -10, 6, -8, 10, 7, -2, 6, 17, 7, 11, 3, 1, 9, 9, 16, 18, 11, 16, 4, 16, 9, 9, 7, 6, 16, 6, -1, 10, 8, 16, 12, 12, 13, 3, 0, -6]


    count=fast_count_segments(starts, ends, points)
    naive_count=naive_count_segments(starts, ends, points)

    assert count==naive_count

    print('test3 pass')

def test_random():

    for trials in range(0,10000):

        seg_size=random.randrange(1,100)

        starts=[]
        ends=[]
        points=[]

        for x in range (0,seg_size):
            
            start_end_valid=False
            while start_end_valid==False:
                start_number=random.randrange(-100,200)
                end_number=random.randrange(-100,200)
                if start_number<end_number:
                    start_end_valid=True
            
            starts.append(start_number)
            ends.append(end_number)
        

        assert len(starts)==len(ends)

        points_size=random.randrange(20,80)

        for x in range(0,points_size):
            points.append(random.randrange(-300,300))






        count=fast_count_segments(starts, ends, points)
        naive_count=naive_count_segments(starts, ends, points)

        if count!=naive_count:
            print('fail random test')
            print(starts)
            print(ends)
            print(points)

        assert count==naive_count

    print('test_random pass')

if __name__=='__main__':
    test1()
    test2()
    test3()
    test_random()