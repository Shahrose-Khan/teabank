from fastapi import APIRouter, HTTPException
from app.models.inventory import Inventory
from app.services import inventory_service

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.post("/")
async def create(entry: Inventory):
    return await inventory_service.create_inventory(entry)


@router.get("/{id}")
async def get(id: str):
    result = await inventory_service.get_inventory(id)
    if not result:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return result


@router.get("/")
async def get_all():
    return await inventory_service.get_all_inventory()


@router.put("/{id}")
async def update(id: str, entry: Inventory):
    success = await inventory_service.update_inventory(id, entry)
    if not success:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return {"success": success}


@router.delete("/{id}")
async def delete(id: str):
    success = await inventory_service.delete_inventory(id)
    if not success:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return {"success": success}
