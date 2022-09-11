print("*******************Namste! Welcome to the tip caculator********************************")
billAmount=float(input("What was the total bill amount ? $"))
tipPercent=int(input("What percentage tip would you like to give ? "))
noOfPeople=int(input("How many person to split the bill ? "))

contributaion=( billAmount + billAmount*tipPercent/100)/noOfPeople

# print(billAmount)
# print(tipPercent)
# print(noOfPeople)

print(f"Each person should pay :${contributaion}")