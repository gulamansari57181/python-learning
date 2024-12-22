# To Generate all the sub sequence of list [3,2,1]
# [],[3],[2],[1],[3,2],[3,1],[3,2,1],[2,1]


numbers=[3,2,1]
sequence=[]

def subsequence(idx,numbers,ls):
    
    if idx==len(numbers):
    # If do not pass copy of ls, it will inplace reference to ls and result will be drastically weired.   
        sequence.append(ls.copy())
        return
        
     # Take an element and add to list
    ls.append(numbers[idx])
        
    subsequence(idx+1,numbers,ls)
        
    # Once return back, we are not taking the added element and again generating the list
    ls.pop()
    subsequence(idx+1,numbers,ls)
        

# Function call
subsequence(0,numbers,[])

print(sequence)
    