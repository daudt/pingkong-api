import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config # Using sync engine for this env.py
from sqlalchemy import pool

from alembic import context
from sqlmodel import SQLModel

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
if PROJECT_ROOT not in sys.path: # Ensure it's added only once if script runs multiple times
    sys.path.insert(0, PROJECT_ROOT)
print(f"[env.py] PROJECT_ROOT: {PROJECT_ROOT}")
print(f"[env.py] sys.path: {sys.path}")

# Crucial: Import all model files to ensure SQLModel.metadata is populated
# The order might matter if there are direct class dependencies not handled by strings/TYPE_CHECKING
# MatchUserLink is in match.py, so match.py should be imported before user.py if user.py refers to MatchUserLink
print("[env.py] Importing app.models.match (contains MatchUserLink)...")
from app.models import match # This imports app/models/match.py
print("[env.py] Imported app.models.match.")
print(f"[env.py] SQLModel.metadata.tables after match: {list(SQLModel.metadata.tables.keys())}")


print("[env.py] Importing app.models.user...")
from app.models import user # This imports app/models/user.py
print("[env.py] Imported app.models.user.")
print(f"[env.py] SQLModel.metadata.tables after user: {list(SQLModel.metadata.tables.keys())}")


print("[env.py] Importing app.models.ranking...")
from app.models import ranking # This imports app/models/ranking.py
print("[env.py] Imported app.models.ranking.")
print(f"[env.py] SQLModel.metadata.tables after ranking: {list(SQLModel.metadata.tables.keys())}")


print("[env.py] Importing app.models.winner...")
from app.models import winner # This imports app/models/winner.py
print("[env.py] Imported app.models.winner.")
print(f"[env.py] SQLModel.metadata.tables after winner: {list(SQLModel.metadata.tables.keys())}")

print("[env.py] Importing app.models.test_model (if exists)...")
try:
    from app.models import test_model # This imports app/models/test_model.py
    print("[env.py] Imported app.models.test_model.")
except ImportError:
    print("[env.py] app.models.test_model not found, skipping.")


print(f"[env.py] SQLModel.metadata.tables after all model imports: {list(SQLModel.metadata.tables.keys())}")

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

try:
    from app.db.database import DATABASE_URL
    # Ensure DATABASE_URL is synchronous for this env.py
    db_url_for_alembic = DATABASE_URL.replace('+aiosqlite', '')
    print(f"[env.py] Imported DATABASE_URL, using: {db_url_for_alembic}")
except ImportError:
    print("[env.py] Could not import DATABASE_URL from app.db.database, using fallback os.getenv")
    db_url_for_alembic = os.getenv('DATABASE_URL', 'sqlite:///./test.db').replace('+aiosqlite', '')
    print(f"[env.py] Using DATABASE_URL: {db_url_for_alembic}")

config.set_main_option('sqlalchemy.url', db_url_for_alembic)
target_metadata = SQLModel.metadata

# Check if metadata is populated before configuring context
if not target_metadata.tables:
    print("[env.py] FATAL: SQLModel.metadata is empty before context.configure(). This will fail autogenerate.")
    # sys.exit(1) # Optionally exit if metadata is empty

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    print("[env.py] Running migrations offline")
    run_migrations_offline()
else:
    print("[env.py] Running migrations online")
    run_migrations_online()

print("[env.py] env.py execution finished.")
print(f"[env.py] Final SQLModel.metadata.tables: {list(SQLModel.metadata.tables.keys())}")
