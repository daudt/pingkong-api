from sqlmodel import create_engine, SQLModel, Session
import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db").replace('+aiosqlite', '')
engine = create_engine(DATABASE_URL, echo=True)
def create_db_and_tables(): SQLModel.metadata.create_all(engine)
def get_db():
    with Session(engine) as session: yield session
print('[db/database.py] Updated with get_db.')
