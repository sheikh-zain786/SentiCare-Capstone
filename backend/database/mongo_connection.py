from pymongo import MongoClient

client = MongoClient("mongodb://10.117.86.221:27017/")
db = client["senticare"]
collection = db["cbt_templates"]

print(collection.find_one())