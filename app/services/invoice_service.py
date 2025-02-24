from app.config import get_database
from app.models.invoice import Invoice
from bson import ObjectId
from pymongo.errors import DuplicateKeyError

db = get_database()
invoice_collection = db["invoices"]

# Ensure bill_no is unique
invoice_collection.create_index("bill_no", unique=True)

# Ensure `bill_no` is unique
invoice_collection.create_index("bill_no", unique=True)

def convert_date_fields(invoice_dict):
    """
    Converts all `date` fields in the invoice dictionary to ISO strings
    for MongoDB compatibility.
    """
    for key in ["date", "delivery_date"]:
        if key in invoice_dict and invoice_dict[key]:
            invoice_dict[key] = invoice_dict[key].isoformat()
    return invoice_dict

async def create_invoice(invoice: Invoice):
    try:
        # Convert date fields
        invoice_dict = convert_date_fields(invoice.dict())
        result = await invoice_collection.insert_one(invoice_dict)
        return {"id": str(result.inserted_id)}
    except DuplicateKeyError:
        return {"error": "Invoice with this bill_no already exists"}
async def get_invoice(bill_no: str):
    return await invoice_collection.find_one({"bill_no": bill_no}, {"_id": 0})

async def get_all_invoices():
    return await invoice_collection.find({}, {"_id": 0}).to_list(100)

async def update_invoice(bill_no: str, invoice: Invoice):
    result = await invoice_collection.update_one(
        {"bill_no": bill_no}, {"$set": invoice.dict()}
    )
    return result.modified_count > 0

async def delete_invoice(bill_no: str):
    result = await invoice_collection.delete_one({"bill_no": bill_no})
    return result.deleted_count > 0
