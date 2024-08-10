# Consider below input point, we have to represent this graph's dfs
pts=[[1,2],[2,3],[3,5],[1,6],[6,4]]
print("Input edges :")
print(pts)
graph={}
vertices=6

# DFS Traversal of the graph

def dfs(graph,node,visited):
    print(node)
    visited.add(node)
    
    # To explore all the childs of this node
    for child in graph[node]:
        if child not in visited:
            dfs(graph,child,visited)
    

# Empty graph initialization
for i in range(1, vertices+1):
    graph[i]=[]
    
print("Empty graph :")
print(graph)

# Putting edges with the help of inputs points connect
for (u,v) in pts:
    graph[u].append(v)
    graph[v].append(u)

print("Graph after Edges Connected :")
print(graph)

# Now we will make a recursive dfs function which has 1)graph, start node and visited set

print("Graph's DFS Traversal :")
dfs(graph,1,set())


