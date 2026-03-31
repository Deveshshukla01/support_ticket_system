from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class TicketCreate(BaseModel):
    title: str
    description: str

class TicketStatusUpdate(BaseModel):
    status: str

class AssignTicket(BaseModel):
    agent_id: int

class CommentCreate(BaseModel):
    content: str