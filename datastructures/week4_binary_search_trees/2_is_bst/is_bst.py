#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def inOrderTraversal(tree, index, result):
  if index == -1:
    return
  
  inOrderTraversal(tree, tree[index][1], result)
  result.append(tree[index][0])
  inOrderTraversal(tree, tree[index][2], result)

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  #print (tree)
  if tree==[]:
    return True
  result=[]
  index=0

  try:
    inOrderTraversal(tree, index, result)
  except:
    print('Error in inOrderTraversal')
  valid=True
  
  for i in range(0,len(result)-1):
    if result[i]>=result[i+1]:
      valid=False
      break
  

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
