
import random

names=input("Enter name of your friends to find out who will pay the bill(Comma seprated):\n")

name_list=names.split(", ")

random_name=random.randint(0,len(name_list))

print(f"{name_list[random_name].title()} is going to buy the meal  today!")



