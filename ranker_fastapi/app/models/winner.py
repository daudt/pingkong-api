print('Executing app/models/winner.py')
from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel
import uuid

if TYPE_CHECKING:
    from .user import User, UserReadBasic
    from .match import Match

class WinnerBase(SQLModel):
    pass

class Winner(WinnerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    match_id: int = Field(foreign_key="match.id", index=True, unique=True)
    user: "User" = Relationship(back_populates="won_matches")
    match: "Match" = Relationship(back_populates="winner_record")

class WinnerCreate(SQLModel):
    user_id: int
    match_id: int

class WinnerRead(WinnerBase):
    id: int
    user_id: int
    match_id: int

class WinnerReadBasic(SQLModel):
    user: "UserReadBasic"
print('Finished executing app/models/winner.py')
