from tree_height import *

def test1():
    tree=[-1,0,4,0,3]
    result=compute_height_original(len(tree),tree)

    resultb=compute_height_tree_optimally(len(tree),tree)

    assert result==resultb

    print (result)


def test2():
    tree=[8,8,5,6,7,3,1,6,-1,5]
    result=compute_height_original(len(tree),tree)

    resultb=compute_height_tree_optimally(len(tree),tree)

    assert result==resultb

    print (result)

def test3():
    tree=[4,-1,4,1,1]
    result=compute_height_original(len(tree),tree)

    resultb=compute_height_tree_optimally(len(tree),tree)

    assert result==resultb

    print (result)

def test_debug():
    tree=[-1,0,4,0,3]
    
    btree=class_binary_tree()

    for x in tree:
        btree.add(x)

    print('height=%d'%btree.compute_height())

def test_compute_height_make_tree():
    tree=[4,-1,4,1,1]
    
    btree=compute_height_make_tree(tree)


    
    que=compute_height_tree_make_que(btree)

    print(que)

    layers=compute_height_tree_from_child(que[-1])

    print(layers)




  

  

if __name__=="__main__":
    test1()
    test2()
    test3()
    #test_debug()
    #test_compute_height_make_tree()


    print ('end')



