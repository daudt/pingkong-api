from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import Table, Column, Integer, ForeignKey
import uuid # Ensure uuid is imported

# Define the association table using SQLAlchemy core
# This table needs to be associated with SQLModel.metadata
match_user_link_table = Table(
    "matchuserlink", # Table name
    SQLModel.metadata,
    Column("match_id", Integer, ForeignKey("match.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("user.id"), primary_key=True),
)

if TYPE_CHECKING:
    from .user import User, UserReadBasic
    from .winner import Winner, WinnerReadBasic

# MatchUserLink SQLModel class is removed.

class MatchBase(SQLModel):
    confirmed: bool = Field(default=False)

class Match(MatchBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    match_uuid: uuid.UUID = Field(default_factory=uuid.uuid4, index=True, unique=True) # Renamed from uuid

    # Use sa_relationship_kwargs with the secondary table
    users: List["User"] = Relationship(
        back_populates="matches",
        sa_relationship_kwargs={
            "secondary": match_user_link_table
        }
    )
    winner_record: Optional["Winner"] = Relationship(back_populates="match", sa_relationship_kwargs={"uselist": False})

class MatchCreate(MatchBase):
    user_ids: List[int]

class MatchRead(MatchBase):
    id: int
    match_uuid: uuid.UUID
    users: List["UserReadBasic"] = []
    winner: Optional["UserReadBasic"] = None
    losing_user: Optional["UserReadBasic"] = None

class MatchUpdate(SQLModel):
    confirmed: Optional[bool] = None

class MatchReadWithoutUsers(MatchBase):
    id: int
    match_uuid: uuid.UUID
    winner: Optional["UserReadBasic"] = None
print('[models/match.py] Recreated with SQLAlchemy Table for link model.')
