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
        self.head=new_node
        self.tail=new_node
        # To keep the track of the nlength of the node
        self.length=1
        
       
    
    def append(self,value):
       
        #To Create a node and insert it to end of linkedlist 
        new_node= Node(value)
        
        # To check if linkedlist is empty
        if self.head is  None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next = new_node
            self.tail=new_node
        self.length +=1
        return True
          
            
          
    
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
    
    def print_list(self):
        temp=self.head
        print("Linkedlist elements are :")
        while temp is not None:
            print(temp.value,end=" ")
            temp=temp.next
            

list1 = LinkedList(4)  
list1.append(5) 
print(f"Head of linked list contains :{list1.head.value}")
print(f"Tail of linked list contains :{list1.tail.value}")
print(f"Length of linked list is :{list1.length}")

list1.print_list()