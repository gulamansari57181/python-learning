numbers=[10,20,30,5,60,25,90]


def max(idx,numbers):
    if idx==len(numbers)-1:
        return numbers[idx]
    
    misa=max(idx+1,numbers)
    
    if misa>numbers[idx]:
        return misa
    else :
        return numbers[idx]
    
    
ans=max(0,numbers)

print(f"Maximu element is :{ans}")