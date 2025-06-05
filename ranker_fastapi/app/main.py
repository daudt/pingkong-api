from fastapi import FastAPI
from app.db.database import engine
from app.routers import users, matches # Added matches
from sqlmodel import SQLModel

app = FastAPI(title="Ranker API")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
async def root():
    return {"message": "Welcome to Ranker API"}

app.include_router(users.router, prefix="/api")
app.include_router(matches.router, prefix="/api") # Added matches router
print('[main.py] Updated with matches router.')
