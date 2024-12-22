numbers=[10,20,30,5,60,25,90]


def maximum(idx,numbers):
    if idx==len(numbers)-1:
        return numbers[idx]
    
    # Recursion leap of faith, that somehow idx+1 to end, I know the mazimum
    # Then I will only compare that value to current index value to get maximum.
    misa=maximum(idx+1,numbers)
    
    if misa>numbers[idx]:
        return misa
    else :
        return numbers[idx]
    
    
ans=maximum(0,numbers)

print(f"Maximu element is :{ans}")