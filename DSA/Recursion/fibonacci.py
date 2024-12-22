# Write a recursive program to find nth fibonacci number

# Time Complexity O(2^n)

def fibo(n,dp):
    
    if n<2:
        return n
    
    if(dp[n]!=-1):
        # To avoid already solved problem, function call getting invoked
        return dp[n]
    
    dp[n] = fibo(n-1,dp) + fibo(n-2,dp)
    
    return dp[n]


n=int(input("Write which term of fibonacci series you want to know:"))
dp=[-1]*(n+1)
print(fibo(n,dp))
