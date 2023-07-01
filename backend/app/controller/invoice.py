from fastapi import APIRouter, HTTPException
from app.model.invoice import Invoice
from app.config import db, commit_rollback
from sqlalchemy.future import select
from app.schema.invoice import InvoiceResponse, InvoiceRequest, ResponseSchema
from app.service.invoice import InvoiceService

router = APIRouter(prefix="", tags=["Invoice"])


@router.post("/invoice", response_model=ResponseSchema)
async def create_invoice(product_data: InvoiceRequest):
    invoice = Invoice(**product_data.dict())
    db.session.add(invoice)
    await commit_rollback()
    await db.session.refresh(invoice)
    return ResponseSchema(detail="Successfully fetch data!")


# @router.get("/invoice/{invoice_id}", response_model=InvoiceResponse)
# async def get_invoice_by_id(invoice_id: str):
#     query = select(Invoice).where(Invoice.invoice_id == invoice_id)
#     result = await db.session.execute(query)
#     invoice = result.scalars()

#     if invoice:
#         return invoice
#     else:
#         raise HTTPException(status_code=404, detail="Invoice not found")

@router.get("/invoice/{invoice_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_invoice(invoice_id: str):
    result = await InvoiceService.get_invoice(invoice_id)
    return ResponseSchema(detail="Successfully fetch data!", result=result)
