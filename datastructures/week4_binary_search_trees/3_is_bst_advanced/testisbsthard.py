import importlib  
import pathlib
import threading, sys
isbst = importlib.import_module("is_bst_hard")



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
    """
    CREATING A BIG TREE
    """
    treesize=1000000
    tree=[]
    for i in range(treesize):
        tree.append([i+1,-1,-1])
    
        if 2*i+1<treesize:
            tree[i][1]=2*i+1
        if 2*i+2<treesize:
            tree[i][2]=2*i+2
    print(tree)

    valid=isbst.IsBinarySearchTree(tree)
    print(valid)


def open_21_tree():
    """
    open 21 text file and create a tree
    """
    #print current path
    #print(pathlib.Path(__file__).parent.absolute())
    f=open('/home/philip/training/datastructures/week4_binary_search_trees/2_is_bst/21','r') #for some reason i have to use absolute path    print(f.read())
    size=(f.readline())

    tree=[]
    for line in f:
        tree.append(list(map(int,line.strip().split())))
    f.close()

    valid=isbst.IsBinarySearchTree(tree)
    assert valid==False
    print("finished open_21_tree test   <<<< if no see no pass")

def duplicate_keys():
    #duplicates on the left are not allowed
    tree=[[2,1,2],[2,-1,-1],[3,-1,-1]]
    valid=isbst.IsBinarySearchTree(tree)
    assert valid==False

    #duplicates on the right are allowed
    tree=[[2,1,2],[1,-1,-1],[2,-1,-1]]
    valid=isbst.IsBinarySearchTree(tree)
    assert valid==True
    
def main():

    test_in_order_traversal()
    test_isbinarysearchtree()
    #bigtree()
    open_21_tree()
    duplicate_keys()
    print('Test passed')


if __name__ == "__main__":
    threading.Thread(target=main).start()