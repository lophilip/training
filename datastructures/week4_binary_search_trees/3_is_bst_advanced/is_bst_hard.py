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
    self.recursion=0
    self.duplicates={}  #dict of duplicates, key is the index to result, value is true or false if value[key+1] is allowed duplicate
    #allowed duplicates are only allowed on the right side of the tree
    

  def inOrderTraversal(self,index=0):
    if index == -1:
      return
    
    self.inOrderTraversal(self.tree[index][1])
    self.result.append(self.tree[index][0])

    if len(self.result)>=2:
      if self.result[-1]==self.result[-2]:
        self.duplicates[len(self.result)-2]=False
    
    lenresult=len(self.result)
    self.inOrderTraversal(self.tree[index][2])
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
  

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  #print (tree)
  if tree==[]:
    return True
  result=[]
  index=0
  valid=True

  """
  try:
    inOrderTraversal(tree, index, result)
  except:
    print('Error in inOrderTraversal')
  valid=True
  
  for i in range(0,len(result)-1):
    if result[i]>=result[i+1]:
      valid=False
      break
  """
  binarytree=binarytreeclass(tree)
  
  result=binarytree.inOrderTraversal()
  valid=binarytree.checkBST()
  
  
  

  return valid


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

if __name__== '__main__':
  threading.Thread(target=main).start()
