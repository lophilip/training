import reachability

def test1():
    adj = [[1, 3], [0, 2], [1, 3], [2, 0]]
    x=0
    y=3
    assert reachability.reach(adj, x, y) == 1


if __name__ == '__main__':
    test1()
    print("Test 1 passed...")