# To Connect mongoDB using python's PyMongo driver and perform basic crud operation.
print("Welcome to PyMongo Module")

# Step 1: import pymong module
import pymongo as pm

# Step2: Connect with mongoDB client, here 
# "mongodb://localhost:27017" is connection string of local instance of mongod process
client=pm.MongoClient("mongodb://localhost:27017")
print(client)

# Step 3: Creating a database name:techConfusion
# Note: In MongoDB, a database is not created until it gets content!
techConfusion=client["techConfusion"]
print(client.list_database_names())

# Step4:  To create a collection and insert one record (documen) in that collection.
web_dev=techConfusion["WebDev"]

# Creating a document in terms of dictionary structure
tech1={"name":"html","compelition_time":"6-7 days","learning_curve":"easy"}
web_dev.insert_one(tech1)