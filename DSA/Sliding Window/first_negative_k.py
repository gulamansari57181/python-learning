nums=[]

size=int(input("Enter size of the number list :"))

for i in range(size):
    nums.append(int(input(f"Enter {i+1} element :")))

k=int(input("Enter value of k :"))
    
i=0
j=0
negatives=[]
ans=[]

while(j<size):
    # To perform basic calculatio. i.e if negative push it into negative number list
    if(nums[j]<0):
        negatives.append(nums[j])
    
    if(j-i+1<k):
        j +=1
    else:
        # Figure out answer from calculation.
        # To check if no negative element in current window
        if(len(negatives)==0):
            ans.append(0)
        else:
            ans.append(negatives[0])
        
        
             # imp arr[i] == nrgatives[0], 
             # then we need to remove this negative value from the negative list
            if nums[i]==negatives[0]:
                negatives.pop(0)
        i +=1
        j+=1

print(ans)
        
        