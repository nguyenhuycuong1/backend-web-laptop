from fastapi import APIRouter
from app.model.invoice import Invoice
from app.config import db, commit_rollback
from app.schema.invoice import InvoiceResponse, InvoiceRequest, ResponseSchema

router = APIRouter(prefix="", tags=["Invoice"])


@router.post("/invoice", response_model=ResponseSchema)
async def create_invoice(product_data: InvoiceRequest):
    invoice = Invoice(**product_data.dict())
    db.session.add(invoice)
    await commit_rollback()
    await db.session.refresh(invoice)
    return ResponseSchema(detail="Successfully fetch data!")
