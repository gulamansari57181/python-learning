# Recursive approach to print string in reverse manner

msg=input("Enter your message :")


def reverse(m,idx):
    
    # Will try to go to end caharcater than return from that
    # Thus our base condition become
    
    if idx>=len(m):
        return
    
    # Faith -> It will somehow gives reverse of "idx +1" character, after that I will print last character
    
    reverse(m,idx+1)
    print(m[idx], end="")
    
# Function call
print("Reverse of the string is :")
reverse(msg,0)

