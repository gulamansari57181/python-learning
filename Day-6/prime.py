# Imorting math module

import math
number = int(input("Please Enter a number : "))

def isPrime(number):
    for i in range(2, int(math.sqrt(number))):
        if number %i == 0:
            return f"Number {number} is not a Prime number."
    return f"Number {number}  is a prime number."

#Method call 
answer = isPrime(number)
print(answer)
