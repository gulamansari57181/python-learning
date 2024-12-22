# To Generate all the Sub Sequence sum= k containing duplicate
# [],[3],[2],[1],[3,2],[3,1],[3,2,1],[2,1]


numbers=[3,2,1,1,4,2,5]
sequence=[]
k=5

def subsequence(idx,ls,sum):
    
    if idx==len(numbers) :
        if k==sum:
            print(ls)
            return True
        else:
            return False        
            
                        
    
    else:
            # Take an element and add to list
        sum += numbers[idx]
        
        ls.append(numbers[idx])
        
        if(subsequence(idx+1,ls,sum)):
            return True
        
        # Once return back, we are not taking the added element and again generating the list
        sum -= numbers[idx]
        ls.pop()
        
        if(subsequence(idx+1,ls,sum)):
            return True
        
        return False   
    
        
    

# Function call
subsequence(0,[],0)


    