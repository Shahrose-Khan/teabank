from app.config import get_database
from app.models.business import Business
from bson import ObjectId
from pymongo.errors import DuplicateKeyError

db = get_database()
business_collection = db["businesses"]

# Optional: ensure uniqueness if `id` is part of your model
business_collection.create_index("id", unique=True)

# Helper to convert ObjectId to string in returned documents
def transform_document(document):
    if document:
        document["_id"] = str(document["_id"])
    return document

# Create a new business
async def create_business(business: Business):
    try:
        result = await business_collection.insert_one(business.dict())
        return {"id": str(result.inserted_id)}
    except DuplicateKeyError:
        return {"error": "Business with this ID already exists"}

# Get a business by MongoDB _id
async def get_business(id: str):
    try:
        object_id = ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId format")

    document = await business_collection.find_one({"_id": object_id})
    return transform_document(document)

# Get all businesses with _id as string
async def get_all_businesses():
    cursor = business_collection.find()
    businesses = []
    async for document in cursor:
        businesses.append(transform_document(document))
    return businesses

# Update a business by _id
async def update_business(id: str, business: Business):
    try:
        object_id = ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId format")

    result = await business_collection.update_one(
        {"_id": object_id}, {"$set": business.dict()}
    )
    return result.modified_count > 0

# Delete a business by _id
async def delete_business(id: str):
    try:
        object_id = ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId format")

    result = await business_collection.delete_one({"_id": object_id})
    return result.deleted_count > 0
