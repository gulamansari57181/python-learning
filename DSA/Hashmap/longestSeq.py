# WAP to find longest sequence of number in a list
# e.g. arr=[1,5,7,3,8,10,11,12,6,13,14] ams -> 10,11,12,13,14 with length=5

# To take numers as an input

size=int(input("Enter size of number list : "))

numbers=[]
for number in range(size):
    numbers.append(int(input("Enter element : ")))


# To initialze a hasmap with all the number as key and longest sequence start as true
hm={}
for number in numbers:
    hm[number] ='True'
        

# To make non-starting sequence numbers "False" 
# i.e. 9 and 10 both exist then 10 can not be start of the sequence so make it as false  

for number in numbers:
    if (number -1) in hm.keys():
        hm[number]='False'


# To traverse on only true value and find maximum sequence length and starting value
ml=0
msp=numbers[0]
for number in numbers:
    
    if hm[number]=="True":
        tl=1
        tsp=number
        
        while((tsp + tl) in hm.keys()):
            tl +=1
        
        if(tl>ml):
            msp=tsp
            ml=tl
            

#To print longest sequence 


print("Longest csequence of number is as follows : ")
for i in range(msp,msp+ml+1):
    print(i,end=" ")   