# Time complexity: O(logn)
# List must be sorted

size = int(input("Enter size of the list :"))

numbers = []
for i in range(size):
    num = int(input("Enter element of the array :"))
    numbers.append(num)


def binary_search(arr, element, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            end = mid - 1
        else:
            start = mid + 1

    return -1


# get element to be search
ele = int(input("Enter elment to be search :"))

index = binary_search(numbers, ele, 0, len(numbers) - 1)

print(f"Element is present at {index} position.")
  