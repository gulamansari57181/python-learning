
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# column=int(input("Please enter column number from 1 to 3: "))
# row = int(input("Please enter row number from 1 to 3: "))

map[int(position[1])-1][int(position[0])-1]='X-Coin'


# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")