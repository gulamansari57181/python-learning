'''
Task- To find wether graph is bipartite or not

Implementation: If graph is 2 Colorable-> Bipartite else Not Bipartite.

**** ImpAppraoach -> a) Maintain a parent and visited.
                     b) Run dfs and give alternate color to the nodes
                     c) if node[color]==child[color] -> Not Bi-partite 
'''

edges=[[1,2],[2,3],[3,4]]
nodes=[1,2,3,4]

graph={}



for u,v in edges:
    if u not in graph:
        graph[u]=[]
    
    if v not in graph:
        graph[v]=[]
    
    graph[u].append(v)
    graph[v].append(u)

print(graph)

def bipartite(graph,node,visited,color,c):
    visited[node]=1
    color[node]=c
    
    for child in graph[node]:
        if child not in visited:
            temp=bipartite(graph,child,visited,color,c^1)
            # If any function call return false our graph is not bipartite
            if temp==False:
                return False
        else:
            # If our node and its child color are same then- Not bipartite
            if color[node]==color[child]:
                return False
                
            
start=1
visited={}
color={}
graph_status=bipartite(graph,start,visited,color,0)

if graph_status==False:
    print("No- Graph is not bipartite.")
else:
    print("Yes- Graph is bipartite.")