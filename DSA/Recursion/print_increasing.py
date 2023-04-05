 #A program to print numbers upto n in recursive manner

num=int(input("Enter number upto whic we have to print numbesrs: "))

def print_increasing(n):
    # Base condition
    if n==0:
        return
    # Recursive call (Head Recursion)
    print_increasing(n-1)
    
    print(n)
    
    
    
    
def print_decreasing(n):
    # Base condition
    if n==0:
        return
   
    print(n)
     # Recursive call (Tail Recursion)
    print_decreasing(n-1)
    
 
# Method call
print_increasing(num)
print("*"*50)
print_decreasing(num)