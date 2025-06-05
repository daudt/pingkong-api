from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel
import datetime

if TYPE_CHECKING:
    from .user import User, UserReadBasic # Added UserReadBasic

class RankingBase(SQLModel):
    rating: float
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class Ranking(RankingBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)

    user: "User" = Relationship(back_populates="rankings")

class RankingCreate(RankingBase):
    user_id: int

class RankingRead(RankingBase):
    id: int
    user_id: int
    # user: Optional["UserReadBasic"] = None # Could add basic user info
