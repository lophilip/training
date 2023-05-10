import importlib  
treeorders = importlib.import_module("tree-orders")

def test1_tree_orders():
    tree = treeorders.TreeOrders()

    treetyple=((4,1,2),(2,3,4),(5,-1,-1),(1,-1,-1),(3,-1,-1))

    for x in range(len(treetyple)):
        tree.add(treetyple[x][0],treetyple[x][1],treetyple[x][2])
    
    inorder=tree.inOrder()
    assert inorder==[1,2,3,4,5]
    print(inorder)

    preOrder=tree.preOrder()
    print(preOrder)
    assert preOrder==[4,2,1,3,5]

    postOrder=tree.postOrder()
    print(postOrder)
    assert postOrder==[1,3,2,5,4]



def test2_tree_orders():
    tree = treeorders.TreeOrders()

    treetyple=(0,7,2),(10,-1,-1),(20,-1,6),(30,8,9),(40,3,-1),(50,-1,-1),(60,1,-1),(70,5,4),(80,-1,-1),(90,-1,-1)

    for x in range(len(treetyple)):
        tree.add(treetyple[x][0],treetyple[x][1],treetyple[x][2])
    
    inorder=tree.inOrder()
    print(inorder)
    assert inorder==[50,70,80,30,90,40,0,20,10,60]
    
    preOrder=tree.preOrder()
    print(preOrder)
    assert preOrder==[0,70,50,40,30,80,90,20,60,10]

    postOrder=tree.postOrder()
    print(postOrder)
    assert postOrder==[50,80,90,30,40,70,10,60,20,0]

if __name__=='__main__':
    test1_tree_orders()
    test2_tree_orders()
    print('Test passed')
