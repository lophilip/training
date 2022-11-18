import change


def test_getchange_2():
    coins=change.get_change(2)

    assert(coins==2),'should be 2 coins'

    print('test_getchange_2 pass')

def test_getchange_28():
    coins=change.get_change(28)

    assert(coins==6),'should be 6 coins'

    print('test_getchange_28 pass')


if __name__=='__main__':
    test_getchange_2()
    test_getchange_28()