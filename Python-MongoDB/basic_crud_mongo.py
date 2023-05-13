# To Connect mongoDB using python's PyMongo driver and perform basic crud operation.
print("Welcome to PyMongo Module")

# Step 1: import pymong module
import pymongo as pm

# Step2: Connect with mongoDB client, here 
# "mongodb://localhost:27017" is connection string of local instance of mongod process
client=pm.MongoClient("mongodb://localhost:27017")
print(client)

# Step 3: Creating a database name:techConfusion

# techConfusion=