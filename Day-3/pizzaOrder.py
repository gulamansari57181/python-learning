from copyreg import pickle


print("************************ Welcom to Pizza Mania ***************************")

pizzaSize= input("What size of pizza do you want ? S, M or L: ")
pepperoni = input("Do you want pepperoni ? Y or N: ")
extraCheese = input("DO you want extra cheese ? Y or N :")

billAmount=0

if pizzaSize=='S':
    # small pizza price = $15
    billAmount=15
    if pepperoni=='Y':
        # Add $2 for pepperoni
        billAmount +=2
elif pizzaSize=='M':
    # medium pizza price = $20
    billAmount=20
    if pepperoni=='Y':
        # Add $3 for pepperoni
        billAmount +=3
else:
    # large pizza price = $25
    billAmount=25
    if pepperoni=='Y':
        # Add $3 for pepperoni
        billAmount +=3

if extraCheese=='Y':
    billAmount += 1
    
print(f"Your final bill is ${billAmount}")              