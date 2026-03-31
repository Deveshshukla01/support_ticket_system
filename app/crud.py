from sqlalchemy.orm import Session
import app.models as models
import bcrypt

def create_user(db: Session, user):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_password.decode('utf-8')
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def login_user(db: Session, user):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    
    if not db_user:
        return None
    
    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password.encode('utf-8')):
        return None
    
    return db_user

def create_ticket(db: Session, ticket, user_id: int):
    db_ticket = models.Ticket(
        title=ticket.title,
        description=ticket.description,
        user_id=user_id
    )
    
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def get_all_tickets(db: Session):
    return db.query(models.Ticket).all()

def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()

def assign_ticket(db: Session, ticket_id: int, agent_id: int):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    
    if ticket:
        ticket.agent_id = agent_id
        db.commit()
    
    return ticket

def update_ticket_status(db: Session, ticket_id: int, status: str):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    
    if ticket:
        ticket.status = status
        db.commit()
    
    return ticket

def filter_tickets(db: Session, status: str):
    return db.query(models.Ticket).filter(models.Ticket.status == status).all()