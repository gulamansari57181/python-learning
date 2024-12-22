str=input("Enter a string :")

def palindrome(str,left,right):
    
    if left>=right:
        return True
    
    if str[left]==str[right]:
        return palindrome(str,left+1,right-1)
    else:
    
        return False


if palindrome(str,0,len(str)-1):
    print(f"{str} is palindrome string!!")
else:
    print(f"{str} is not palindrome string!!")