from app.config import get_database
from app.models.user import User

db = get_database()
users_collection = db["users"]

async def get_all_users():
    return await users_collection.find().to_list(100)

async def create_user(user: User):
    result = await users_collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}
