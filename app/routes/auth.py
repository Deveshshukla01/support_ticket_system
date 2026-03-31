from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import app.schemas as schemas
import app.crud as crud

router = APIRouter()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    crud.create_user(db, user)
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.login_user(db, user)
    
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"message": "Login successful"}