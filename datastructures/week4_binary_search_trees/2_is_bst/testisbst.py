import importlib  
isbst = importlib.import_module("is_bst")

def test_in_order_traversal():
    tree=[[2,1,2],[1,-1,-1],[3,-1,-1]]
    result=[]
    index=0
    isbst.inOrderTraversal(tree, index, result)
    print(result)
    assert result==[1,2,3]



    tree=[[1,1,2],[2,-1,-1],[3,-1,-1]]
    result=[]
    index=0
    isbst.inOrderTraversal(tree, index, result)
    print(result)
    assert result==[2,1,3]


    tree=[[1,-1,1],[2,-1,2],[3,-1,3],[4,-1,4],[5,-1,-1]]
    result=[]
    index=0
    isbst.inOrderTraversal(tree, index, result)
    print(result)
    assert result==[1,2,3,4,5]


    tree=[[4,1,2],[2,3,4],[6,5,6],[1,-1,-1],[3,-1,-1],[5,-1,-1],[7,-1,-1]]
    result=[]
    index=0
    isbst.inOrderTraversal(tree, index, result)
    print(result)
    assert result==[1,2,3,4,5,6,7]


    tree=[[4,1,-1],[2,2,3],[1,-1,-1],[5,-1,-1]]
    result=[]
    index=0
    isbst.inOrderTraversal(tree, index, result)
    print(result)
    assert result==[1,2,5,4]


def test_isbinarysearchtree():
    tree=[[2,1,2],[1,-1,-1],[3,-1,-1]]
    result=[]
    index=0
    valid=isbst.IsBinarySearchTree(tree)
    assert valid==True


    tree=[[1,1,2],[2,-1,-1],[3,-1,-1]]
    result=[]
    index=0
    valid=isbst.IsBinarySearchTree(tree)
    assert valid==False

    tree=[[1,-1,1],[2,-1,2],[3,-1,3],[4,-1,4],[5,-1,-1]]
    result=[]
    index=0
    valid=isbst.IsBinarySearchTree(tree)
    assert valid==True

    tree=[[4,1,2],[2,3,4],[6,5,6],[1,-1,-1],[3,-1,-1],[5,-1,-1],[7,-1,-1]]
    result=[]
    index=0
    valid=isbst.IsBinarySearchTree(tree)
    assert valid==True

    tree=[[4,1,-1],[2,2,3],[1,-1,-1],[5,-1,-1]]
    result=[]
    index=0
    valid=isbst.IsBinarySearchTree(tree)
    assert valid==False



def bigtree():
    tree= \
    


if __name__=='__main__':
    test_in_order_traversal()
    test_isbinarysearchtree()
    print('Test passed')