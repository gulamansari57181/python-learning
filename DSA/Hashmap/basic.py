# To create a hashmap

# Approach 1: using dict() keyword
hm=dict()

# Approcah 2: using {}
hm1={}

print(type(hm))
print(type(hm1))

# Inserting element in to dict in terms of key-value pair

hm["India"]=145
hm["China"]=142
hm["Pakistan"]=25

print(hm)

# Update value  at a key

hm["India"]=143
print(hm)

# To Get all the key value pair
print(list(hm.items()))

# To Get all the keys
print(list(hm.keys()))

# To get all the values
print(list(hm.values()))

# To get key based on value 

key=[k for k,v in hm.items() if v==25]
print(key)
print(key[0])

# Toupdate a particular key value
print(hm.get(key[0]))