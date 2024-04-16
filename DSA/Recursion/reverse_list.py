numbers=[1,2,5,6,12,23,54,"Mango"]


def reverse_list(ls,left,right):
    
    if left>=right:
        return ls
    
    print(ls[right])
    temp=ls[left]
    ls[left]=ls[right]
    ls[right]=temp
    
    return reverse_list(ls,left+1,right-1)
    
    
    
    
reverse_numbers=reverse_list(numbers,left=0,right=len(numbers)-1)


print(f"Reverse of the  list is : {reverse_numbers} ")