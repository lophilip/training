#Uses python3

import sys

class graphnodeclass:
    def __init__(self,n):
        self.adj=[]        
        self.removed=False  #flags to indicate if node has been removed
        self.index=n    #index of node in the list
    def add_adj(self,adj):
        if adj not in self.adj: #do not do duplicate adj
            self.adj.append(adj)

    def remove_adj(self,n):
        if n in self.adj:
            self.adj.remove(n)


def number_of_components(adj):
    num_edges=len(adj)
    num_vertices=-1
    for i in adj:
        for j in i:
            if j>num_vertices:
                num_vertices=j
    num_vertices+=1

    return num_vertices,num_edges


def transverse_withoutbacktracking(node,index,visited=[], path=[]): #pass test 1 to 10, fail 11
    sink=False
    repeat=False

    currentnode=node[index]

    if index not in visited:
            visited.append(index)           
    
    if currentnode.adj==[]:
        sink=True
    else:        
        for i in currentnode.adj:            
            if repeat:
                break
            if i not in visited and repeat==False:
                repeat = transverse(node,i,visited,path)
            else:
                repeat=True            
            
            #path.extend(visited)
            #visited=[]
            """
            if index in visited:
                visited.remove(index) #remove index from visited list
                path.append(index) #add index to path
            """
    
    return repeat

def transverse(node,index,visited=[], path=[]):
    sink=False
    repeat=False

    currentnode=node[index]

    if index not in visited:
            visited.append(index)           
    
    if currentnode.adj==[]:
        sink=True
        path.append(index)
        if index in visited:
                visited.remove(index)
    else:        
        for i in currentnode.adj:            
            if repeat:
                break
            if i not in visited and repeat==False and i != index: #looping back to itself is cycle
                if index not in visited:
                    visited.append(index)
                repeat = transverse(node,i,visited,path)
            else:
                repeat=True            
            
            #path.extend(visited)
            #visited=[]
            path.append(index)
            if index in visited:
                visited.remove(index)
            """
            if index in visited:
                visited.remove(index) #remove index from visited list
                path.append(index) #add index to path
            """
    
    return repeat

def acyclic(adj):   #return 1 if cycle found, 0 if no cycle found

    num_vertices,num_edges=number_of_components(adj)
    


    node=[]
    for i in range(num_vertices):
        node.append(graphnodeclass(i))
    
    for i in adj:
        node[i[0]].add_adj(i[1])
    
    currentnode=0
    visited=[]

    repeat=False
    
    all_visited=False
    
    while repeat==False and all_visited==False:    
        localvisited=[]    
        path=[]
        repeat=transverse(node,currentnode,localvisited,path)
        visited.extend(path)

        for i in path:
            #remove nodes visited from the list
            for j in node:
                j.remove_adj(i)
                pass
        
        if repeat==False: #only find next node if no cycle found
            visitied_norepeats=list()

            #only add unique nodes to visitied_norepeats
            for i in visited:
                if i not in visitied_norepeats:
                    visitied_norepeats.append(i)

            if len(visitied_norepeats)==num_vertices:
                all_visited=True
            else:
                #find next node to transverse
                for i in range(num_vertices):
                    if i not in visitied_norepeats:
                        currentnode=i
                        break

    #print (visited)
    #print (repeat)
        
    return 1 if repeat==True else 0


def move_vertex(vertex, src, dst):
    src.remove(vertex)
    dst.append(vertex)


def acyclic_reference(adj):
    finish = []
    current = []
    set = [x for x in range(len(adj))]

    def explore(v):
        move_vertex(v, set, current)
        for u in adj[v]:
            if u in finish:
                continue
            if u in current:
                return True
            if explore(u):
                return True
        move_vertex(v, current, finish)
        return False

    while len(set) > 0:
        if explore(set[0]):
            return 1
    return 0


if __name__ == '__main__':


    num_vertices, num_edges = (int(i) for i in input().split())
    vertices_split = [(input().split()) for _ in range(num_edges)]
    edges = [[int(i[0]) - 1, int(i[1]) - 1] for i in vertices_split]
    print(acyclic(edges))
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
    """
