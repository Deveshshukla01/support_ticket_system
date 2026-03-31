from fastapi import FastAPI
from database import engine, Base
import auth, tickets

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(tickets.router)

@app.get("/")
def home():
    return {"message": "Support Ticket System API Running"}