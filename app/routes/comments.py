from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
import app.schemas as schemas
import app.models as models

router = APIRouter()

@router.post("/tickets/{ticket_id}/comment")
def add_comment(ticket_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    new_comment = models.Comment(
        content=comment.content,
        ticket_id=ticket_id
    )
    
    db.add(new_comment)
    db.commit()
    
    return {"message": "Comment added successfully"}