#!/usr/bin/python3

import sys, threading

#sys.setrecursionlimit(10**7) # max depth of recursion
#threading.stack_size(2**25)  # new thread will get stack of such size


sys.setrecursionlimit(10**7) # max depth of recursion

print('sys.getrecursionlimit(): %d'%sys.getrecursionlimit())
threading.stack_size(2**50)  # new thread will get stack of such size

print('threading.stack_size(): %d'%threading.stack_size())

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

  def inOrderTraversal(self,index=0):
    if index == -1:
      return
    self.recursion+=1
    print('recursion: %d'%self.recursion)

    #if self.recursion>=15830:
    #  print('asldkfj')
      #pass
    
    self.inOrderTraversal(self.tree[index][1])
    self.result.append(self.tree[index][0])
    self.inOrderTraversal(self.tree[index][2])

    return self.result
  
  def checkBST(self):
    for i in range(0,len(self.result)-1):
      if self.result[i]>=self.result[i+1]:
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
  try:
    result=binarytree.inOrderTraversal()
  except Exception as e:
    print('Error in inOrderTraversal: %s'%e)
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

if __name__ == '__main__':
  threading.Thread(target=main).start()
