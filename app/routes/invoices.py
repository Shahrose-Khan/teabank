from fastapi import APIRouter, HTTPException
from app.models.invoice import Invoice
from app.services.invoice_service import (
    create_invoice,
    get_invoice,
    get_all_invoices,
    update_invoice,
    delete_invoice,
)

router = APIRouter(prefix="/invoices", tags=["Invoices"])

@router.post("/")
async def add_invoice(invoice: Invoice):
    return await create_invoice(invoice)

@router.get("/{bill_no}")
async def get_invoice_by_bill_no(bill_no: str):
    invoice = await get_invoice(bill_no)
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

@router.get("/")
async def get_invoices():
    return await get_all_invoices()

@router.put("/{bill_no}")
async def update_invoice_by_bill_no(bill_no: str, invoice: Invoice):
    updated = await update_invoice(bill_no, invoice)
    if not updated:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return {"message": "Invoice updated successfully"}

@router.delete("/{bill_no}")
async def delete_invoice_by_bill_no(bill_no: str):
    deleted = await delete_invoice(bill_no)
    if not deleted:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return {"message": "Invoice deleted successfully"}
