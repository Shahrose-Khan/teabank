from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class InvoiceItem(BaseModel):
    lot_no: str
    no_of_packages: int
    grade: str
    garden: str
    total_weight_kgs: float
    nt_packages: int
    shortage_in_kgs: float
    total_net_weight: float
    rate_per_kg: float
    amount: float

class Invoice(BaseModel):
    bill_no: str
    messers: str
    do_no: Optional[str] = None
    transporter: Optional[str] = None
    date: date
    broker: Optional[str] = None
    payment: Optional[str] = None
    bilty_no: Optional[str] = None
    items: List[InvoiceItem]
    brokerery: Optional[float] = 0.0
    bardan: Optional[float] = 0.0
    godown_rent: Optional[float] = 0.0
    delivery_date: Optional[date] = None
    total_cartage: Optional[float] = 0.0
    net_amount: Optional[float] = 0.0
