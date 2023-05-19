# A program to find kth largest element from an array

# Approach1 : To use heapq
import heapq
# To take array as input
size=int(input("Enter size of an array : "))
numbers=[]

for number in range(size):
    numbers.append(int(input("Enter an element : ")))

k=int(input("Enter kth largest element to find : "))

print(f"Kth largest number in a the array is {heapq.nlargest(k,numbers,key=None)[k-1]}")


