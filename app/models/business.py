from pydantic import BaseModel
from typing import Optional

class Business(BaseModel):
    name: str
    address: str
    area: str
    city: str
    tel: str
    cell: str
    role: str
