# To Generate all the Sub Sequence whose  sum= k also only unique sub sequence.


numbers=[3,2,1,1,4,2,5]
sequence=[]
k=5

def subsequence(idx,ls,sum):
    
    if idx==len(numbers) :
        if k==sum:
            if ls not in sequence:
                sequence.append(ls.copy()) 
        return
                                
    
    
    # Take an element and add to list
    sum += numbers[idx]
    
    ls.append(numbers[idx])
    
    subsequence(idx+1,ls,sum)
        
    # Once return back, we are not taking the added element and again generating the list
    sum -= numbers[idx]
    ls.pop()
    
    subsequence(idx+1,ls,sum)
              
  

# Function call
subsequence(0,[],0)
print(sequence)


    