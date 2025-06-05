import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from sqlmodel import SQLModel
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
if PROJECT_ROOT not in sys.path: sys.path.insert(0, PROJECT_ROOT)
print(f"[env.py] PROJECT_ROOT: {PROJECT_ROOT}")
print(f"[env.py] sys.path: {sys.path}")
print("[env.py] Importing app.models.match (defines match_user_link_table)...")
from app.models import match
print(f"[env.py] Imported app.models.match. SQLModel.metadata.tables: {list(SQLModel.metadata.tables.keys())}")
print("[env.py] Importing app.models.user (uses match_user_link_table)...")
from app.models import user
print(f"[env.py] Imported app.models.user. SQLModel.metadata.tables: {list(SQLModel.metadata.tables.keys())}")
print("[env.py] Importing app.models.ranking...")
from app.models import ranking
print(f"[env.py] Imported app.models.ranking. SQLModel.metadata.tables: {list(SQLModel.metadata.tables.keys())}")
print("[env.py] Importing app.models.winner...")
from app.models import winner
print(f"[env.py] SQLModel.metadata.tables after all model imports: {list(SQLModel.metadata.tables.keys())}")
config = context.config
if config.config_file_name is not None: fileConfig(config.config_file_name)
try:
    from app.db.database import DATABASE_URL
    db_url_for_alembic = DATABASE_URL.replace('+aiosqlite', '')
except ImportError:
    db_url_for_alembic = os.getenv('DATABASE_URL', 'sqlite:///./test.db').replace('+aiosqlite', '')
config.set_main_option('sqlalchemy.url', db_url_for_alembic)
target_metadata = SQLModel.metadata
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"})
    with context.begin_transaction(): context.run_migrations()
def run_migrations_online() -> None:
    connectable = engine_from_config(config.get_section(config.config_ini_section, {}), prefix="sqlalchemy.", poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction(): context.run_migrations()
if context.is_offline_mode(): run_migrations_offline()
else: run_migrations_online()
print("[env.py] env.py execution finished.")
print(f"[env.py] Final SQLModel.metadata.tables: {list(SQLModel.metadata.tables.keys())}")
