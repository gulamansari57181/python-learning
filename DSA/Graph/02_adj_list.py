# Consider below input point, we have to represent this as a graph
pts=[[1,2],[2,3],[3,5],[1,6],[6,4]]

print("Input Points")
print(pts)

# First of all we have to initialize a dict to map nodes and its adjacent edges

graph={}

# Now we will initialize an empty graph of max vertices(here 1-6)
vertices=6
for i in range(1,vertices+1):
    graph[i]=[]

print("Empty Graph :")
for item in graph.items():
    print(item)
    
    
'''
Task1- To iterate over input values let say (u,v) of the graph
Implementation- We can done this with the help of graph.items() method.

And thus we will try to connect edge from u to v
and v to u (Adjacency list) by traversing our input points.
'''

for (u,v) in pts:
    # Edges connection representation, Graph are undirected/ Bi-drected
    graph[u].append(v)
    graph[v].append(u)

print("Complete Graph :")
print(graph)