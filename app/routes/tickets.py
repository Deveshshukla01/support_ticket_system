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

@router.get("/tickets")
def get_all_tickets(db: Session = Depends(get_db)):
    return crud.get_all_tickets(db)

@router.get("/tickets/filter")
def filter_tickets(status: str, db: Session = Depends(get_db)):
    return crud.filter_tickets(db, status)

@router.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.get_ticket_by_id(db, ticket_id)
    
    if not ticket:
        return {"error": "Ticket not found"}
    
    return ticket

@router.put("/tickets/{ticket_id}/assign")
def assign_ticket(ticket_id: int, data: schemas.AssignTicket, db: Session = Depends(get_db)):
    ticket = crud.assign_ticket(db, ticket_id, data.agent_id)
    
    if not ticket:
        return {"error": "Ticket not found"}
    
    return {"message": "Ticket assigned successfully"}

@router.put("/tickets/{ticket_id}/status")
def update_status(ticket_id: int, data: schemas.TicketStatusUpdate, db: Session = Depends(get_db)):
    ticket = crud.update_ticket_status(db, ticket_id, data.status)
    
    if not ticket:
        return {"error": "Ticket not found"}
    
    return {"message": "Status updated successfully"}

