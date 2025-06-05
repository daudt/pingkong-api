from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
import uuid

if TYPE_CHECKING:
    from .user import User, UserReadBasic
    from .winner import Winner, WinnerReadBasic

# This is the link model. It must be defined before User and Match try to use it by string.
class MatchUserLink(SQLModel, table=True):
    match_id: Optional[int] = Field(default=None, primary_key=True, foreign_key="match.id")
    user_id: Optional[int] = Field(default=None, primary_key=True, foreign_key="user.id")

class MatchBase(SQLModel):
    confirmed: bool = Field(default=False)

class Match(MatchBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    match_uuid: uuid.UUID = Field(default_factory=uuid.uuid4, index=True, unique=True) # Changed from uuid to match_uuid

    users: List["User"] = Relationship(back_populates="matches", link_model="MatchUserLink")
    winner_record: Optional["Winner"] = Relationship(back_populates="match", sa_relationship_kwargs={"uselist": False})

class MatchCreate(MatchBase):
    user_ids: List[int]

class MatchRead(MatchBase):
    id: int
    match_uuid: uuid.UUID # Changed
    users: List["UserReadBasic"] = []
    winner: Optional["UserReadBasic"] = None
    losing_user: Optional["UserReadBasic"] = None

class MatchUpdate(SQLModel):
    confirmed: Optional[bool] = None

class MatchReadWithoutUsers(MatchBase):
    id: int
    match_uuid: uuid.UUID # Changed
    winner: Optional["UserReadBasic"] = None
