# Write a recursive program to find nth fibonacci number

# Time Complexity O(2^n)

def fibo(n):
    
    if n<2:
        return n
    return fibo(n-1) + fibo(n-2)


n=int(input("Write which term of fibonacci series you want to know:"))
print(fibo(n))
