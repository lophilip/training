from change_dp import *



def test1():

    change=3

    cnative= get_change_recursive_naive(change)

    cdynamic=get_change_dynamic(change)

    print(cnative)
    print(cdynamic)

    assert cnative==cdynamic


    change=34

    #cnative= get_change_recursive_naive(change)   #this takes much too long
    cnative=9

    cdynamic=get_change_dynamic(change)

    print(cnative)
    print(cdynamic)

    assert cnative==cdynamic


if __name__=='__main__':
    test1()
    