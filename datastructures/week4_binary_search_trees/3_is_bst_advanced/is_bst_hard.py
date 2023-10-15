#!/usr/bin/python3

import sys, threading

#sys.setrecursionlimit(10**7) # max depth of recursion
#threading.stack_size(2**25)  # new thread will get stack of such size


sys.setrecursionlimit(10**9) # max depth of recursion

#print('sys.getrecursionlimit(): %d'%sys.getrecursionlimit())
threading.stack_size(2**27)  # new thread will get stack of such size

#print('threading.stack_size(): %d'%threading.stack_size())

def inOrderTraversal(tree, index, result):
  if index == -1:
    return
  
  inOrderTraversal(tree, tree[index][1], result)
  result.append(tree[index][0])
  inOrderTraversal(tree, tree[index][2], result)


class binarytreeclass:
  def __init__(self, tree):
    self.tree=tree
    self.result=[]
    self.result_left_transitions=[]  #list of left transitions
    self.result_right_transitions=[]  #list of right transitions
    self.recursion=0
    self.duplicates={}  #dict of duplicates, key is the index to result, value is true or false if value[key+1] is allowed duplicate

    #allowed duplicates are only allowed on the right side of the tree

    self.left_transitions=0
    self.right_transitions=0
    

  def inOrderTraversal(self,index=0):
    if index == -1:
      return
    
    self.left_transitions+=1
    self.inOrderTraversal(self.tree[index][1])
    self.left_transitions-=1
    self.result.append(self.tree[index][0])
    self.result_left_transitions.append(self.left_transitions)
    self.result_right_transitions.append(self.right_transitions)

    if len(self.result)>=2:
      if self.result[-1]==self.result[-2]: 
        self.duplicates[len(self.result)-2]=False
        if self.result_right_transitions[-1] > self.result_right_transitions[-2]: #allow duplicates on the right side of tree
          self.duplicates[len(self.result)-2]=True
    
    lenresult=len(self.result)
    self.right_transitions+=1
    self.inOrderTraversal(self.tree[index][2])
    self.right_transitions-=1
    lenresult2=len(self.result)
    if len(self.result)>=2:
      if self.result[-1]==self.result[-2] and lenresult2>lenresult:
        self.duplicates[len(self.result)-2]=True
    


    return self.result
  
  

  def checkBST(self):
    for i in range(0,len(self.result)-1):
      if self.result[i]>self.result[i+1]:
        return False
      if self.result[i]==self.result[i+1]:
        if i in self.duplicates:
          if self.duplicates[i]==False:
            return False
        
    return True
  

def IsBinarySearchTree(tree, printresult=True):
  # Implement correct algorithm here
  #print (tree)
  if tree==[]:
    return True
  result=[]
  index=0
  valid=True

  binarytree=binarytreeclass(tree)
  
  result=binarytree.inOrderTraversal()  

  if printresult:
    print(result)
    print(binarytree.duplicates)
  valid=binarytree.checkBST()
  
  
  

  return valid


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree,printresult=False):
    print("CORRECT")
  else:
    print("INCORRECT")

if __name__== '__main__':
  threading.Thread(target=main).start()
