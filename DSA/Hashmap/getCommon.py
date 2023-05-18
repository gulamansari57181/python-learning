# A program to find common element from two array
# arr1=[1,1,1,2,3,5,6,7,8] and arr2=[1,2,3,4,5,6,,8,9] ans -> 1,2,3,5,6,8

# To get element of array1 and array2 

size1=int(input("Enter size of first array: "))
arr1=[]
for i in range(size1):
    arr1.append(input("Enter an element :"))
 
    
size2=int(input("Enter size of second array: "))
arr2=[]
for i in range(size2):
    arr2.append(input("Enter an element :"))
    
def get_common(arr1,arr2):
    hm={}
    common_elements=[]
    # To make frequency map of arr1
    for element in arr1:
        if element in hm:
            hm[element] +=1
        else:
            hm[element]=1
    # To print and remove key from hm while traversing in arr2
    for value in arr2:
        if value in hm.keys():
            common_elements.append(value)
            del hm[value]
            
    
    return common_elements

ans=get_common(arr1,arr2)
# print(*ans)
print(f"Common element in both the array are : {ans}")