from fastapi import APIRouter, HTTPException
from app.models.business import Business
from app.services.business_service import (
    create_business,
    get_business,
    get_all_businesses,
    update_business,
    delete_business,
)

router = APIRouter(prefix="/business", tags=["Business"])


@router.post("/")
async def add_business(business: Business):
    return await create_business(business)


@router.get("/{id}")
async def get_business_by_id(id: str):
    business = await get_business(id)
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    return business


@router.get("/")
async def get_businesses():
    return await get_all_businesses()


@router.put("/{id}")
async def update_business_by_id(id: str, business: Business):
    updated = await update_business(id, business)
    if not updated:
        raise HTTPException(status_code=404, detail="Business not found")
    return {"message": "Business updated successfully"}


@router.delete("/{id}")
async def delete_business_by_id(id: str):
    deleted = await delete_business(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Business not found")
    return {"message": "Business deleted successfully"}
