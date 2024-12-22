
#Kth size subarray maximum-sum
num=[]
size=int(input("Enter Number Of Elements :"))

for i in range(size):
    ele=int(input(f"Enter-{i+1} element :"))
    num.append(ele)

k=int((input("Enter sub array size(k)")))
max_sum=float("-inf")

i=0
j=0
cur_sum=0

while(j<len(num)):
    cur_sum +=num[j]
    
    if(j-i+1<k):
        # Window is not hit yet.
        j +=1
    elif (j-i+1==k):
        # Window is hit
        max_sum=max(cur_sum,max_sum)
        # removing 'i'th location value, from current sum
        cur_sum -=num[i]
        # move the window of constant size
        i +=1
        j +=1

            
    
print(max_sum)
        