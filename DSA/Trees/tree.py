# To create a binary tree

class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        

# Creating a dummy Node

t=BinaryTree("A")

print(t.value)
print(t.left)
print(t.right)