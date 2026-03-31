from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
import app.schemas as schemas
import app.crud as crud

router = APIRouter()

@router.post("/tickets")
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    crud.create_ticket(db, ticket, user_id=1)
    return {"message": "Ticket created successfully"}