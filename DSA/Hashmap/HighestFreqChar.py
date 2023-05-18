# WAP to find highest frequency character from a string
# e.g. aabbaaccdefg -> ans= "a" with frequency 4

# To take input string
str=input("Enter charcter string :")

# To make frequency map
fmap={}

for letter in str:
    if letter in fmap:
        fmap[letter] +=1
    else:
        fmap[letter]=1

# To get maximum value from hashmap
max_value=max(fmap.values())

# To get key from value
highest_freq_char=[key for key,val in fmap.items() if val==max_value][0]

print(f"Highest occuring  character in the string is : '{highest_freq_char}' with frequency {max_value}")