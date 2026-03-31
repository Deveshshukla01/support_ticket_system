from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import app.schemas as schemas
import app.crud as crud

router = APIRouter()

@router.post("/tickets")
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
    
    if not ticket.title or not ticket.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    
    if not ticket.description or not ticket.description.strip():
        raise HTTPException(status_code=400, detail="Description cannot be empty")

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
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    return ticket

@router.put("/tickets/{ticket_id}/assign")
def assign_ticket(ticket_id: int, data: schemas.AssignTicket, db: Session = Depends(get_db)):
    
    if data.agent_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid agent ID")

    ticket = crud.assign_ticket(db, ticket_id, data.agent_id)
    
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    return {"message": "Ticket assigned successfully"}

@router.put("/tickets/{ticket_id}/status")
def update_status(ticket_id: int, data: schemas.TicketStatusUpdate, db: Session = Depends(get_db)):
    
    valid_status = ["open", "in_progress", "closed"]

    # ✅ Check if status is valid
    if data.status not in valid_status:
        raise HTTPException(status_code=400, detail="Invalid status")

    ticket = crud.update_ticket_status(db, ticket_id, data.status)
    
    # ✅ Check if ticket exists
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    return {"message": "Status updated successfully"}

@router.get("/tickets/user/{user_id}")
def get_user_tickets(user_id: int, db: Session = Depends(get_db)):
    tickets = crud.get_tickets_by_user(db, user_id)
    
    if not tickets:
        return {"message": "No tickets found for this user"}
    
    return {
        "message": "User tickets fetched successfully",
        "data": tickets
    }

@router.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    
    ticket = crud.delete_ticket(db, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    return {"message": "Ticket deleted successfully"}