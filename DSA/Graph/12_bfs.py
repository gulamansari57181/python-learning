'''
Try to implement bfs on graph
DS- Queue
'''

edges=[[1,2],[2,3],[3,4]]
nodes=[1,2,3,4]

# Initialize the graph
graph={}
visited={}
start=1

for i in range(1,len(nodes)+1):
    graph[i]=[]
    visited[i]=False

for (u,v) in edges:
    graph[u].append(v)
    graph[v].append(u)

print(graph)


def bfs(graph,visited,start):
    # we will initialize a queue and first element to it
    # Also mark it as visited
    
    q=[]
    q.append(start)
    visited[start]=True
    
    
    # Now we have to pop this element as it is visited and
    # Add its connected(child) node into the queue
    # And repeat this untill our queue is not empt
    while q:
        # Removing the parent element which is visited
       
        node=q.pop(0)
        print(node)
        
        # To visit all the node's which are connected to this poped node
        for child in graph[node]:
            if not  visited[child]:
                # Append or insert into the queue and marked them visited
                q.append(child)
                visited[child]=True
                
            
    
print(graph)
bfs(graph,visited,start)