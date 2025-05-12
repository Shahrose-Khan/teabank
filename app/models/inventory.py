from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

class Inventory(BaseModel):
    purchase_id: str
    quantity: int
    date: datetime
    godown_id: str
    type: Literal["in", "out"]
