from pymongo import MongoClient
client = MongoClient()

db = client["Department_Report"]
msg_collection = db["Department_level_Report"]

# Create a message dict
message = {
    "Department": "All",
    "Feedback": "DB Schenker Best Company Forever",
    "Risk_Level": "Low"
}

result = msg_collection.insert_one(message)
print(result.inserted_id)

import pprint
pp = pprint.PrettyPrinter(indent=4)
for doc in msg_collection.find():
    pp.pprint(doc)