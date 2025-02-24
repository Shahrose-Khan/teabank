from fastapi import FastAPI
from app.routes.invoices import router as invoice_router

app = FastAPI()

# Include invoice routes
app.include_router(invoice_router, prefix="/invoices", tags=["Invoices"])

@app.get("/")
def read_root():
    return {"message": "Invoice Management System"}
