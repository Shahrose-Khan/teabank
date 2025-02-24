from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.services.user_service import get_all_users, create_user

router = APIRouter()

@router.get("/")
async def get_users():
    return await get_all_users()

@router.post("/")
async def add_user(user: User):
    return await create_user(user)
