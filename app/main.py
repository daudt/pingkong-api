from fastapi import FastAPI
from app.db.database import create_db_and_tables
# Import routers later when they are defined
# from app.routers import users, matches, rankings, history

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Ranker API"}

# app.include_router(users.router, prefix="/api")
# app.include_router(matches.router, prefix="/api")
# app.include_router(rankings.router, prefix="/api")
# app.include_router(history.router, prefix="/api")
