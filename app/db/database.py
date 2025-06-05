from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import create_async_engine # Import for async engine
import os
from dotenv import load_dotenv

load_dotenv()

# Use aiosqlite for async operations
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db")

# Create an async engine
engine = create_async_engine(DATABASE_URL, echo=True) # Set echo=False for production


# The create_db_and_tables function in SQLModel is synchronous.
# For async, you typically manage table creation with Alembic or use sync connections for setup.
# For now, we'll keep the sync version for create_db_and_tables,
# but it should ideally be run with a sync engine or handled by Alembic.
# This function might not be directly usable with an async engine for metadata creation
# without specific handling. Alembic will handle table creation.

def create_db_and_tables():
    # This is a synchronous operation. For initial setup or testing,
    # you might create a temporary sync engine or manage schema with Alembic.
    # For simplicity in this step, we'll acknowledge Alembic is the primary tool.
    # from sqlmodel import create_engine as create_sync_engine_temp
    # temp_sync_engine = create_sync_engine_temp(DATABASE_URL.replace("+aiosqlite", ""))
    # SQLModel.metadata.create_all(temp_sync_engine)
    # print("Note: create_db_and_tables() called with a temporary sync engine for setup if not using Alembic.")
    # However, since we are using Alembic, this function becomes less critical for schema creation.
    # We'll leave it, but Alembic migrations are the source of truth.
    print("Table creation is primarily handled by Alembic. Ensure migrations are run.")
    pass
