from app.config import get_database
from app.models.invoice import Invoice
from bson import ObjectId
from pymongo.errors import DuplicateKeyError

db = get_database()
invoice_collection = db["invoices"]

# Ensure bill_no is unique (if used externally)
invoice_collection.create_index("bill_no", unique=True)


# Convert ObjectId to string
def transform_document(doc):
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc


# Convert datetime fields to ISO strings
def convert_date_fields(invoice_dict):
    for key in ["date", "delivery_date"]:
        if key in invoice_dict and invoice_dict[key]:
            invoice_dict[key] = invoice_dict[key].isoformat()
    return invoice_dict


# Create invoice
async def create_invoice(invoice: Invoice):
    try:
        invoice_dict = convert_date_fields(invoice.dict())
        result = await invoice_collection.insert_one(invoice_dict)
        return {"id": str(result.inserted_id)}
    except DuplicateKeyError:
        return {"error": "Invoice with this bill_no already exists"}


# Get invoice by _id
async def get_invoice(id: str):
    try:
        object_id = ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId format")

    doc = await invoice_collection.find_one({"_id": object_id})
    return transform_document(doc)


# Get all invoices
async def get_all_invoices():
    invoices = []
    async for doc in invoice_collection.find():
        invoices.append(transform_document(doc))
    return invoices


# Update invoice by _id
async def update_invoice(id: str, invoice: Invoice):
    try:
        object_id = ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId format")

    invoice_dict = convert_date_fields(invoice.dict())
    result = await invoice_collection.update_one(
        {"_id": object_id}, {"$set": invoice_dict}
    )
    return result.modified_count > 0


# Delete invoice by _id
async def delete_invoice(id: str):
    try:
        object_id = ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId format")

    result = await invoice_collection.delete_one({"_id": object_id})
    return result.deleted_count > 0
