from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tickets")
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    new_ticket = models.Ticket(
        title=ticket.title,
        description=ticket.description,
        user_id=1
    )
    
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    
    return {"message": "Ticket created successfully"}