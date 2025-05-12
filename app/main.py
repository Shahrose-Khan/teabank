from fastapi import FastAPI
from app.routes import invoices, business, role, inventory

app = FastAPI()

# Include routes
app.include_router(invoices.router)
app.include_router(business.router)
app.include_router(role.router)
app.include_router(inventory.router)

@app.get("/")
def read_root():
    return {"message": "Invoice Management System"}
