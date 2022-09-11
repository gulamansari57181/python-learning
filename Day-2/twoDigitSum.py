number=input("Enter a number :\n")
twoDigitSum=0

# Logic to find digitSum : 123 => 1+2+3=6
for i in range(0,len(number)):
    
    twoDigitSum +=int(number[i]) 

print(f"Digit Sum is : {twoDigitSum}")