
print("******************* Welcome to the world of Love **************************************")
yourName= input("Enter your name: ")
partnerName = input("Please enter your partner name: ")

name = yourName.lower()
partner = partnerName.lower()

lCount=name.count("l") + partner.count("l")
oCount=name.count("o") + partner.count("o")
vCount=name.count("v") + partner.count("v")
eCount=name.count("e") + partner.count("e")
tCount=name.count("t") + partner.count("t")
rCount=name.count("r") + partner.count("r")
uCount=name.count("u") + partner.count("u")

loveTotal= lCount + oCount +vCount + eCount
trueTotal= tCount + rCount + uCount+ eCount

print(f"T occurs {tCount} times\nR occurs {rCount} times\nU occurs {uCount} times\nE occurs {eCount} times")
print(f"Total = {trueTotal}")

print(f"L occurs {lCount} times\nO occurs {oCount} times\nV occurs {vCount} times\nE occurs {eCount} times")
print(f"Total = {loveTotal}")

loveScore = int(str(trueTotal)+str(loveTotal))


if loveScore<10 or loveScore>90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >=40 and loveScore<=50:
     print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your Score is {loveScore}.")
