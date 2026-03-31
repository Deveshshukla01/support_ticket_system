from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth, tickets
from app.routes import comments

Base.metadata.create_all(bind=engine)

app = FastAPI()

from fastapi.responses import JSONResponse
from fastapi import Request

@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal server error",
            "error": str(exc)
        }
    )

app.include_router(auth.router)
app.include_router(tickets.router)
app.include_router(comments.router)

@app.get("/")
def read_root():
    return {"message": "Helpdesk Ticketing API Running"}