from app.config import get_database
from app.models.inventory import Inventory
from bson import ObjectId

db = get_database()
inventory_collection = db["inventory"]


# Helper to convert _id to string
def transform_document(doc):
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc


# Convert datetime fields to ISO
def convert_date_fields(data: dict):
    if "date" in data and data["date"]:
        data["date"] = data["date"].isoformat()
    return data


# Create inventory entry
async def create_inventory(entry: Inventory):
    entry_dict = convert_date_fields(entry.dict())
    result = await inventory_collection.insert_one(entry_dict)
    return {"id": str(result.inserted_id)}


# Get one inventory record by _id
async def get_inventory(id: str):
    try:
        object_id = ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId format")
    doc = await inventory_collection.find_one({"_id": object_id})
    return transform_document(doc)


# Get all inventory entries
async def get_all_inventory():
    inventory = []
    async for doc in inventory_collection.find():
        inventory.append(transform_document(doc))
    return inventory


# Update inventory by _id
async def update_inventory(id: str, entry: Inventory):
    try:
        object_id = ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId format")

    entry_dict = convert_date_fields(entry.dict())
    result = await inventory_collection.update_one(
        {"_id": object_id}, {"$set": entry_dict}
    )
    return result.modified_count > 0


# Delete inventory by _id
async def delete_inventory(id: str):
    try:
        object_id = ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId format")

    result = await inventory_collection.delete_one({"_id": object_id})
    return result.deleted_count > 0
