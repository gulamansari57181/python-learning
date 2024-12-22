# First networkx library is imported 
# along with matplotlib 
import networkx as nx 
import matplotlib.pyplot as plt 


# Defining a Class 
class GraphVisualization: 

    def __init__(self,edges=[]): 
        # Initialize empty edge list
        self.visual = edges
    
    
    
    
    # In visualize function G is an object of 
	# class Graph given by networkx G.add_edges_from(visual) 
	# creates a graph with a given list 
	# nx.draw_networkx(G) - plots the graph 
	# plt.show() - displays the graph 
    def visualize(self):
        G=nx.Graph()
        G.add_edges_from(self.visual) 
        # For formating of node
        format = {"alpha":1,"node_size": 500, "node_color": "green","edge_color":"red"}
        nx.draw_networkx(G,**format)
        plt.show()
		
    
# Driver code 
G = GraphVisualization([["A","B"],["B","C"],["C","A"]])  
# G.addEdge(1, 0) 
G.visualize() 
