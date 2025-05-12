from pydantic import BaseModel, Field
from typing import Optional

class Role(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Role name")
    description: Optional[str] = Field(None, max_length=255, description="Optional description")
