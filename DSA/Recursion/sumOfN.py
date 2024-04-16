num=int(input("Enter a number upto which sum need to be claculated : "))

# Approach 1- 
def sum_of_first(n,sum):
    
    if n==0:
        return sum
    
    return sum_of_first(n-1,sum+n)
    
    
    
# sum=sum_of_first(num,sum=0)

# Approach-2
def sum_of_first(n):
    
    if n==1:
        return 1 
    
    return n + sum_of_first(n-1)


# sum=sum_of_first(num,sum=0)

sum=sum_of_first(num)
print(f"Sum of first {num} natural numbers is : {sum}")