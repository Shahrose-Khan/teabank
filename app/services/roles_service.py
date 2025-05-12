from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from app.config import get_database
from app.models.role import Role

db = get_database()
role_collection = db["roles"]

# Ensure name is unique
role_collection.create_index("name", unique=True)

def transform_role(doc):
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

async def create_role(role: Role):
    try:
        result = await role_collection.insert_one(role.dict())
        return {"id": str(result.inserted_id)}
    except DuplicateKeyError:
        return {"error": "Role with this name already exists"}

async def get_role(id: str):
    try:
        oid = ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId format")

    return transform_role(await role_collection.find_one({"_id": oid}))

async def get_all_roles():
    roles = []
    async for doc in role_collection.find():
        roles.append(transform_role(doc))
    return roles

async def update_role(id: str, role: Role):
    try:
        oid = ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId format")

    result = await role_collection.update_one({"_id": oid}, {"$set": role.dict()})
    return result.modified_count > 0

async def delete_role(id: str):
    try:
        oid = ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId format")

    result = await role_collection.delete_one({"_id": oid})
    return result.deleted_count > 0
