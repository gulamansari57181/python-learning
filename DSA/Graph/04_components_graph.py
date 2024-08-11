# We will have a forest as an input, 
# We will have to figure out number of components present in the forest(Disconnected graph)

pts=[["A","B"],["A","C"],["C","D"],["D","A"],["F","G"],["G","E"]]
nodes=["A","B","C","D","E","F","G","H"]
graph={}
v=len(nodes)

# To calculate no of nodes in each graph

def graph_components(graph,node,visited):
    
    visited.add(node)
    
    total_nodes=0
    for child  in graph[node]:
        if child not in visited:
            total_nodes += graph_components(graph,child,visited)
    
    return total_nodes +1
    
    

# To initialize empty graph
for i in range(v):
    graph[nodes[i]]=[]

print(graph)

# To make edge connection

for (u,v) in pts:
    graph[u].append(v)
    graph[v].append(u)

print(graph)

# To calculate number of nodes in each component. 
# If we visit any node of connected component it in return share all the nodes of it.
visited=set()

ans=[]
for node in nodes:
    if node not in visited:
        ans.append(graph_components(graph,node,visited))
        

print("Total Components and number of nodes in that component :")

print(f"Total Components: {len(ans)}")

for i in range(len(ans)):
    print(f"No of nodes in {i+1} Component is {ans[i]}")
    
# start="H"
# print(graph_components(graph,start,visited))