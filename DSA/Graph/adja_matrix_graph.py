#To define a class Grap

class Graph:
    def __init__(self,vertex):
        # Initialize default vertex_count and 
        # its corresponding adjency matrix(list of lists)
        
        self.v_count=vertex
        self.adj_matrix=[[0]*vertex for v in range(vertex)]
    
    # To add a single edge in the graph
    
    def add_edge(self,u,v,w=1):
        # To check if nodes reference is valid or not
        if 0<=u<self.v_count and 0<=v<self.v_count:
            # As it is un directed weighted graph
            self.adj_matrix[u][v]=self.adj_matrix[v][u]=w
        else:
            print("Invalid Vertex !!")
    
    # To remove a single edge from the graph
    def remove_edge(self,u,v):
        # To check if nodes reference is valid or not
        if 0<=u<self.v_count and 0<=v<self.v_count:
            # As it is un directed weighted graph
            self.adj_matrix[u][v]=self.adj_matrix[v][u]=0
        else:
            print("Invalid Vertex !!")
    # To check edge is present or not between two vertices
    def has_edge(self,u,v):
        if 0<=u<self.v_count and 0<=v<self.v_count:
            return self.adj_matrix[u][v] !=0
        else:
            print("Invalid Vertex !!")
    # To print the graph in terms of adjancey matrices
    
    def print_graph(self):
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))


g1=Graph(4)

g1.add_edge(0,1)
g1.add_edge(1,2)
g1.add_edge(2,3)
g1.add_edge(3,1)
# To print the graph
g1.print_graph()