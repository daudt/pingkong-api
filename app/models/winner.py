from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel
import uuid # Added import for uuid

if TYPE_CHECKING:
    from .user import User, UserReadBasic # Added UserReadBasic
    from .match import Match # MatchReadWithoutWinner - maybe not needed if WinnerRead is basic

class WinnerBase(SQLModel):
    pass

class Winner(WinnerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    match_id: int = Field(foreign_key="match.id", index=True, unique=True)

    user: "User" = Relationship(back_populates="won_matches")
    match: "Match" = Relationship(back_populates="winner_record")

class WinnerCreate(SQLModel): # Inherit from SQLModel directly
    user_id: int
    match_id: int

class WinnerRead(WinnerBase):
    id: int
    user_id: int
    match_id: int
    # user: Optional["UserReadBasic"] = None # Populated by service
    # match_uuid: Optional[uuid.UUID] = None # Populated by service from match.uuid

# A simpler version for MatchRead to show winner details
class WinnerReadBasic(SQLModel): # Inherit from SQLModel directly
    user: "UserReadBasic" # Show basic info of the winning user
