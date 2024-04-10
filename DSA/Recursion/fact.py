# A program to calculate factorial of a number


num= int(input("Enter a number: "))


def fact(n):
    # Base Case
    if n==0 or n==1:
        return 1
    
    # Faith that it will somehow give me factorial of "n-1"
    ans=n*fact(n-1)
    
    return ans
    
    
    
    
print(f"Factorial of given number is :{fact(num)}")