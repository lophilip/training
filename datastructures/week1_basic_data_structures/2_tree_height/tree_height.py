# python3

import sys
import threading


def compute_height_original(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


class class_binary_tree_node:
    def __init__(self,value):
        self.lower=None
        self.higher=None
        self.value=value


class class_binary_tree:
    def __init__(self,value=None):
        self.root=class_binary_tree_node(value)

        self.max_level=1
        if value is None:
            self.max_level=0
    
    def _add(self,value,node,layers=1):
        if node.value is None: #first entry in tree
            node.value=value
            self.max_level=1
            return node

        if value>node.value:
            if node.higher is not None:
                self._add(value,node.higher,layers+1)
            else:
                node.higher=class_binary_tree_node(value)
                if layers+1>self.max_level:
                    self.max_level=layers+1
                return node.higher
        else:
            if node.lower is not None:
                self._add(value,node.lower,layers+1)
            else:
                node.lower=class_binary_tree_node(value)
                if layers+1>self.max_level:
                    self.max_level=layers+1
                return node.lower
        

    def add(self,value):
        node=self.root

        self._add(value,node)


    def compute_height(self):
        height=self.max_level
        return height

        

def compute_height_btree(n, parents):
    tree=parents
    btree=class_binary_tree()

    for x in tree:
        btree.add(x)
    
    height=btree.compute_height()

    return height

def compute_height(n, parents):
    return compute_height_tree_optimally(n,parents)


class class_mtree:
    def __init__(self):
        self.child=[]
        self.parent=None
        self.index=None

    def addchild(self,node):        
        self.child.append(node)

    def addparent(self,node):
        self.parent=node

    def setindex(self,index):
        self.index=index

        

def compute_height_make_tree(parents):
    node=[]
    
    for i in range(len(parents)):
        tempnode=class_mtree()
        node.append(tempnode)
    root = node[0]

    for child_index in range(len(parents)):
        parent_index=parents[child_index]
        if parent_index == -1:
            root=node[child_index]
            root.setindex(child_index)
        else:
            node[parent_index].addchild(node[child_index])
            node[child_index].addparent(node[parent_index])
            node[child_index].setindex(child_index)

    return root

def compute_height_tree_make_que(root):

    que=[]

   
    que.append(root)
    
    children=list(root.child)

    while len(children)>0:

        addchild=children.pop(0)
        
        que.append(addchild)

        children.extend(addchild.child)


    return que


def compute_height_tree_from_child(child):    

    node=child

    layer=0
    while node is not None:
        layer+=1
        node=node.parent

    
    
    return layer
    


def compute_height_tree_optimally(n,parents):

    #first make tree
    tree=compute_height_make_tree(parents)

    #make que - level transveral
    
    que=compute_height_tree_make_que(tree)

    #backtrack tree from last node in q
    layers=compute_height_tree_from_child(que[-1])

    return layers


        
    
    




def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
