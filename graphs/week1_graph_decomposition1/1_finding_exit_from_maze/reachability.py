#Uses python3

import sys


class graphclass:
    def __init__(self,adj):
        self.adj=adj
    

    def expore(self,node,visited=[]):
        #print('node:%d'%node)

        if node<len(self.adj):            
            if node not in visited:
                visited.append(node)            
            for x in self.adj[node]:
                if x not in visited:
                    self.expore(x,visited)
        
        return visited

def reach(adj, x, y):
    #write your code here
    """
    print (adj)
    print(x)
    print(y)
    """

    path=0
    grass=graphclass(adj)

    visited=grass.expore(x)

    if y in visited:
        path=1

    return path


if __name__ == "__main__":    

    input1 = (input().split())    
    nr_vertices, nr_edges = int(input1[0]), int(input1[1])    
    vertices_split = [(input().split()) for i in range(nr_edges)]    
    edges = [(int(i[0]), int(i[1])) for i in vertices_split]    
    input2 = (input().split())    
    start, stop = int(input2[0]), int(input2[1])    
    adj = [[] for _ in range(nr_vertices)]    
    start, stop = start - 1, stop - 1   
    for (a, b) in edges:        
        adj[a - 1].append(b - 1)        
        adj[b - 1].append(a - 1)   
    print(reach(adj, start, stop))
"""
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
"""
