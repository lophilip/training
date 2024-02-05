#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    pass


class graphnodeclass:
    def __init__(self,n):
        self.adj=[]     
        self.reverse_adj=[]   
        self.removed=False  #flags to indicate if node has been removed
        self.index=n    #index of node in the list
        self.exists=False
    def add_adj(self,adj):
        if adj not in self.adj: #do not do duplicate adj
            self.adj.append(adj)
    def add_reverse_adj(self,adj):
        if adj not in self.reverse_adj:
            self.reverse_adj.append(adj)

    def is_sink(self):
        sink=False
        if len(self.adj)<=0:
            sink=True        
        return sink
    
    def is_source(self):
        source=False
        if len(self.reverse_adj)<=0:
            source=True
        return source

    def remove_adj(self,n):
        if n in self.adj:
            self.adj.remove(n)
        if n in self.reverse_adj:
            self.reverse_adj.remove(n)


def number_of_components(adj):
    num_edges=len(adj)
    num_vertices=-1
    for i in adj:
        for j in i:
            if j>num_vertices:
                num_vertices=j
    num_vertices+=1

    return num_vertices,num_edges

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
    
    return repeat

def transverse_dfs(node,index,path=[]):  #assume graph is DAG/acyclic
    sink=False
    
    while sink==False:
        currentnode=node[index]
        
        if len (currentnode.adj)<=0:
            sink=True
            path.append(index)                    
            for i in range(len(node)):      #need to optimize this loop
                node[i].remove_adj(index) #remove index from all nodes                
        else:        
            nextnode=currentnode.adj[0]
            transverse_dfs(node,nextnode,path) #if not DAG will cycle forever!    
    return sink


def get_edges(nodes):
    edges=[]
    for index in range(len(nodes)):
        i=nodes[index]
        for j in i:
            edges.append([index,j])
    return edges

def toposort_bak1(adj): #adj is nodes
    used = [0] * len(adj)
    order = []
    #write your code here
    nodes=list(adj)

    num_vertices=len(adj)


    edges=get_edges(nodes)

    #num_vertices,num_edges=number_of_components(adj)   

    node=[]
    for i in range(num_vertices):
        node.append(graphnodeclass(i))
        #if i in vertices:
        #    node[i].exists=True
        if i>=0:
            node[i].exists=True
    
    for i in edges:
        node[i[0]].add_adj(i[1])
    
    currentnode=0
    visited=[]

    repeat=False
    
    all_visited=False
    
    while repeat==False and all_visited==False:    
        localvisited=[]    
        path=[]
        repeat=transverse(node,currentnode,localvisited,path)
        
        pathreverse=path[::-1]
        visited=pathreverse+visited

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
                   
    path=[]

    for i in visited:
        if i not in path:
            path.append(i)

    #for i in range(0,len(path)):
    #    path[i]+=1
    return path

def toposort(adj): #adj is nodes
    used = [0] * len(adj)
    order = []
    #write your code here
    nodes=list(adj)

    num_vertices=len(adj)


    edges=get_edges(nodes)

    reversed_edges=[]
    for i in edges:
        reversed_edges.append([i[1],i[0]])

    

    node=[]
    for i in range(num_vertices):
        node.append(graphnodeclass(i))
        #if i in vertices:
        #    node[i].exists=True
        if i>=0:
            node[i].exists=True
    
    for i in edges:
        node[i[0]].add_adj(i[1])
    
    for i in reversed_edges:
        node[i[0]].add_reverse_adj(i[1])
    
    currentnode=0

    all_visited=False

    path=[]
    currentnode=0

    while node[currentnode].is_source()==False and currentnode<num_vertices-1:  #start with source
        currentnode+=1

    #find node that
    while all_visited==False:
        visited=[]
        unvisited=[]
        
        sink=transverse_dfs(node,currentnode,visited)

        path=visited[::-1]+path
    
        #check if all nodes visited
        for i in range(0,num_vertices):     #need to optimize this loop
            if i not in path:
                unvisited.append(i)
        
        if len(unvisited)==0:
            all_visited=True
        else:                     
            for i in range(0,len(unvisited)):
                currentnode=unvisited[i]
                if node[unvisited[i]].is_source()==True:                    
                    break
            assert node[currentnode].is_source()==True, 'currentnode is not source'
    #path_reverse=path[::-1]

    return path
    
    
    
    



if __name__ == '__main__':
    
    num_vertices, num_edges = (int(i) for i in input().split())
    vertices_split = [(input().split()) for _ in range(num_edges)]
    edges = [[int(i[0]) - 1, int(i[1]) - 1] for i in vertices_split]
    adj = [[] for _ in range(num_vertices)]
    for (a, b) in edges:
        adj[a].append(b)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
    
    """
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
    """
