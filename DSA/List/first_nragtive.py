def printFirstNegativeInteger( A, N, K):
    
    temp_list=[]
    answers=[]
    
    i=0
    j=0
    
    while(j<len(A)):
        
        if(A[j]<0):
            
            temp_list.append(A[j])
        
        if(j-i+1<K):
        # Increase window size upto K
            j=j+1
        
        elif(j-i+1==K):
            
            # if temp_list is empty then we will push 0 to answers list
            if len(temp_list)==0:
                
             answers.append(0)
            # Window size hit, now we need to calculate
            else:
                answers.append(temp_list[0])
                if A[i]==temp_list[0]:
                    print(A[i])
                    temp_list.pop(0)
            i=i+1
            j=j+1
            
    return answers

ans=printFirstNegativeInteger( [-8, 2, 3, -6, 10], 5, 2)

print(ans)
