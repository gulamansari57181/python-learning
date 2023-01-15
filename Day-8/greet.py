name = input("May I know your good name please : ")

def greet(name):
    print("*"*50)
    print(f"Hey {name} its been geatt feeling to see you here.")
    print("Evertying eventually will fall into its place.")
    print(f"{name} just keep going on champ !!!")

if all(char.isalpha() or char.isspace() for char in name):
 greet(name)
else:
    print("Invalid input! Kindly enter string input")