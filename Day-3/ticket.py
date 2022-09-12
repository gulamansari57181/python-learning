# If age is more tham or equal to 18 eligible for movie ticket otherwise not

age = int(input("Enter your age : "))

if age >= 18:
    print("Hurrray!!! You got the ticket. Enjoy the movie.")
else:
    print(f" Ooops ! You are under age. We would love to have you for the moovie after {18-age} years.")    