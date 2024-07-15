sol=[]

def twoSum(target,start,num):
        end=len(num)-1

        while(start<end):

            sum=num[start]+num[end]
            

            if sum==target:
                # We got our probable solution
                # We need to take care of duplicate solution from both end(start,end)
                while(start<end and num[start]==num[start+1]):
                    start=start+1
                while(start<end and num[end]==num[end-1]):
                    end=end-1
                if [-target,num[start],num[end]] not in sol:
                    sol.append([-target,num[start],num[end]])
                
                # If sol found, increment start and decrement end
                start=start+1
                end=end-1
                
                
            elif sum>target:
                end=end-1
            else:
                start=start+1
        
        


def threeSum(num):
    # To sort an array of numbers
        num=sorted(num)
       

        for i in range(len(num)):
        # To not calculate for same ith valu
    
         if(i>0 and num[i]==num[i-1]):
          continue
         target=-(num[i])
         twoSum(target,i+1,num)
        
        return sol


ans=threeSum([0,1,1,])
print(ans)