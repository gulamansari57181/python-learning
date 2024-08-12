'''
Run DFS-> If child already in visited and 
it is not the parent node, means cycle exist
'''



edges=[[1,2],[2,3],[3,4]]
nodes=[1,2,3,4,5]

# Initialize the graph

graph={i:[] for i in range(1,len(nodes)+1)}

for (u,v) in edges:
    graph[u].append(v)
    graph[v].append(u)

print(graph)

def check_cycle(graph,node,visited,par):
    visited.add(node)
    
    for child in graph[node]:
        if child not in visited:
            temp=check_cycle(graph,child,visited,node)
            if temp==True:
                return True
        else:
            # Any child which is already visite, and it is not parent
            # Then we are sure that cycle is present in the graph
            
            if child !=par:
                return True
    return False
            
    
    

start=1
visited=set()
par=-1

if check_cycle(graph,start,visited,par):
    print("Cycle Present in the graph.")
else:
    print("No cycle present in the graph.")
