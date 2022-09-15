number = int(input("Please Enter a number: "))

even_sum=0
for i in range(0, number+1, 2):
    print(i)
    even_sum += i
    
print(f"Sum of even numbers is {even_sum}")    
    