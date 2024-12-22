#Kth size subarray maximum-sum

num=[]

size=int(input("Enter Number Of Elements :"))

for i in range(size):
    ele=int(input(f"Enter-{i+1} element :"))
    num.append(ele)

k=int((input("Enter sub array size(k)")))
max_sum=0
for i in range(0,size-k):
    sum=0
    for j in range(i,i+k):
        sum +=num[j]
    
    print(sum)
    
    max_sum=sum if sum>=max_sum else max_sum
    # max_sum=max(sum,max_sum)
    
print(max_sum)
        