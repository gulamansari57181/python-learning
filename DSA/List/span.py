# Take n numbers from user as a list input and print span of them.

# Initialzing an empty list
numbers = []

size = int(input("Enter size of a list of numbers : "))

for i in range(size):
    elements = int(input("Enter the number :"))
    # Adding elements to the numbers list
    numbers.append(elements)


# To find maximum and minimum values

def spanOfList(number_list):
    min = number_list[0]
    max = number_list[0]

    for i in range(1, len(number_list)):
        if number_list[i] > max:
            max = number_list[i]

        if number_list[i] < min:
            min = number_list[i]

    print(f"Maximum value is {max}")
    print(f"Minimum value is {min}")

    return int(max - min)


print(f"Span of the list is {spanOfList(numbers)}")
