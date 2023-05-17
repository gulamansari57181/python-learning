# WAP to find pair of two elements sum equal to target value in sorted array.
# e.g arr=[2,5,8,9,10] target=15 , then pair will be ->(5,10)


# Taking array input

size = int(input("Enter size of the list :"))

numbers = []
for i in range(size):
    num = int(input("Enter element of the array :"))
    numbers.append(num)

target=int(input("Enter target element :"))


# Approach 1: Applying the linear serach - O(n^2)

def twoSumLinear(arr,target):
    
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            
            if target - arr[i]==arr[j]:
                return arr[i],   arr[j]
            
    return -1,-1

x,y = twoSumLinear(numbers,target)
print(f"Elements whose pair sum equal to target are : {x} and {y}")
