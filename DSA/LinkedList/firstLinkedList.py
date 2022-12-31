# To implement LinkedList data structure

# To create a node instance
class Node:
   def __init__(self,value):
        # To create a new node
        self.value=value
        self.next=None
        
# To implement LinkedList class
class LinkedList:
    def __init__(self,value):
        # To create a new node
        new_node = Node(value)
        
        # print(new_node.value)
        # print(new_node.next)
    
    def append(self,value):
        pass
        #To Create a node and insert it to end of linkedlist 
    
    
    def prepend(self,value):
        pass
        # To create a node and insert it to the start of the linked list
        
    def insert(self,index,value):
        pass
        # To create a node and insert it to mentioned location
        
    def pop(self):
        # To delete last node from the linked list
        pass
    
    def remove(self,index):
        # to delete a specific index node
        pass
        

LinkedList(4)       