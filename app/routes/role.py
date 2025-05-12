from fastapi import APIRouter, HTTPException
from app.models.role import Role
from app.services import roles_service

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/")
async def create_role(role: Role):
    result = await roles_service.create_role(role)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@router.get("/{id}")
async def get_role(id: str):
    role = await roles_service.get_role(id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@router.get("/")
async def get_all_roles():
    return await roles_service.get_all_roles()

@router.put("/{id}")
async def update_role(id: str, role: Role):
    updated = await roles_service.update_role(id, role)
    if not updated:
        raise HTTPException(status_code=404, detail="Role not found or unchanged")
    return {"message": "Role updated"}

@router.delete("/{id}")
async def delete_role(id: str):
    deleted = await roles_service.delete_role(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"message": "Role deleted"}
