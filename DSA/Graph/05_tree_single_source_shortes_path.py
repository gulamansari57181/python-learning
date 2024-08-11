'''
Single source shortest path algorith for tree like graph, Which can be handle by parent pointer only.
'''

edges=[["A","B"],["A","C"],["B","D"],["D","G"],["C","E"],["C","F"]]
nodes=["A","B","C","D","E","F","G"]

graph={}

# Declare and initialize distance dictonary also
distance={}
# To initialize empty afjaceny matrix
for n in nodes:
    graph[n]=[]
    distance[n]=None



# To connect edges

for (u,v) in edges:
    graph[u].append(v)
    graph[v].append(u)
    
print(graph)



def sssp(graph,node,d,distance,parent):
    distance[node]=d
    
    for child in graph[node]:
        if child !=parent:
            sssp(graph,child,d+1,distance,node)
            
# The source from which we start will have distance- "0"
start="A"

sssp(graph,"A",0,distance,-1)

print(distance)