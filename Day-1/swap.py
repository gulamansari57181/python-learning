#Swap the value of two variable

a = 20
b = 30
print(f"Before Swapping: a = {a} and b = {b} ")

# First Logic of swapping two numbers :
# temp=a
# a=b
# b=temp

# Second logic :
# a,b=b,a

# Third logic : Using "+ and - operator"
# a = a+b
# b = a-b
# a = a-b

# Forth Logic Using XOR (^) operator
a=a^b
b=a^b
a=a^b

print(f"After Swapping: a = {a} and b = {b} ")