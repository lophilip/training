# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def __init__(self):
    self.n = 0
    self.key = []
    self.left = []
    self.right = []
    self.result = []
  def add(self, key, left, right):    
    self.key.append(key)
    self.left.append(left)
    self.right.append(right)
  
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self,node=None):
    if node is None:
      self.result = []
      node=0
    
    if self.left[node] != -1:
      self.inOrder(self.left[node])
      
    self.result.append(self.key[node])
    
    if self.right[node] != -1:
        self.inOrder(self.right[node])
    

    return self.result              

  def preOrder(self,node=None):
    if node is None:
      self.result = []
      node=0

    self.result.append(self.key[node])
    if self.left[node] != -1:
      self.preOrder(self.left[node])
    if self.right[node] != -1:
      self.preOrder(self.right[node])
                        
    return self.result

  def postOrder(self,node=None):
    if node is None:
      node=0
      self.result = []

    if self.left[node] != -1:
      self.postOrder(self.left[node])
        

    if self.right[node] != -1:
        self.postOrder(self.right[node])
    
    self.result.append(self.key[node])

                
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))


if __name__ == '__main__':
  threading.Thread(target=main).start()
