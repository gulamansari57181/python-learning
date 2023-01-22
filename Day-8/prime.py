# To check given numer is prime or not

num= int(input("Enter a number to check: "))

# Function to check number is prime or not

def calc_prime(number):
    
 for i in range(2,number**2):
    if number % i==0:
        # Not a prime number and returns false
        return False
 
    # If code reaches here so number is prime and we will return True
 return True


isPrime=calc_prime(num)

if isPrime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")