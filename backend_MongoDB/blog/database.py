from pymongo import MongoClient
client = MongoClient()

db = client["slack"]
msg_collection = db["messages"]

# Create a message dict
message = {
    "channel": "dev",
    "author": "cerami",
    "text": "Hello, world!"
}

result = msg_collection.insert_one(message)
print(result.inserted_id)

import pprint
pp = pprint.PrettyPrinter(indent=4)
for doc in msg_collection.find():
    pp.pprint(doc)