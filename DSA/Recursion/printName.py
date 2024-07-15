# To print name 10 times you want to print name

n=int(input("Enter how many times :"))

def printName(n):
    
    if n==0:
        return
    
    printName(n-1)
    print(f"{n} Times: ")
    print("Mohd Gulam")
    
    
printName(n)