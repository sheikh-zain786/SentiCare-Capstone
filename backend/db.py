import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# ============================================
# CONFIGURATION
# ============================================

# OPTION 1: Local MongoDB (Friend's PC)
LOCAL_MONGO_URI = "mongodb://192.168.1.5:27017/"

# OPTION 2: MongoDB Atlas (Recommended)
# ATLAS_MONGO_URI = "your_atlas_connection_string"

# Choose which one to use
MONGO_URI = LOCAL_MONGO_URI
# MONGO_URI = ATLAS_MONGO_URI


# ============================================
# DATABASE CONNECTION
# ============================================

try:
    client = MongoClient(MONGO_URI)
    
    # Test connection
    client.admin.command('ping')
    print("✅ Connected to MongoDB successfully!")

except ConnectionFailure as e:
    print("❌ MongoDB connection failed:", e)
    client = None


# ============================================
# DATABASE & COLLECTIONS
# ============================================

if client:
    db = client["senticare"]

    # Collections
    users_collection = db["users"]
    conversations_collection = db["conversations"]
    cbt_collection = db["cbt_templates"]

else:
    db = None
    users_collection = None
    conversations_collection = None
    cbt_collection = None
