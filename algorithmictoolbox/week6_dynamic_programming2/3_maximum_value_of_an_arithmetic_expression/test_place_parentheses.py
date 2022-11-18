from placing_parentheses import*

def test1():
    ex="5-8+7*4-8+9"

    result=get_maximum_value(ex)

    print(result)

    assert result==200

def test2():
    ex="1+2-3*4-5"

    result=get_maximum_value(ex)

    print(result)

    assert result==6

if __name__=='__main__':
    test1()
    test2()
    