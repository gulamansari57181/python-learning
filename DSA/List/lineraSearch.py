# Find element in the  list (Linear Search)
number = []
size = int(input("Enter number of elements :"))

# To get all the elements
for i in range(size):
    number.append(int(input(" Enter the number : ")))
    
data = int(input("Enter value to search : "))

for i in range(len(number)):
    if data == number[i]:
        print(f"Elememt is present at the {i+ 1} index")
        # Exit for first occurance
        exit()

# If data is not present in the list
print(" Element is not present in the list")

