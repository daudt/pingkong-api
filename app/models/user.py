from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel
import uuid

# Forward declarations for type checking
if TYPE_CHECKING:
    from .match import Match, MatchUserLink, MatchReadWithoutUsers
    from .ranking import Ranking, RankingRead
    from .winner import Winner

class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    name: Optional[str] = None
    nickname: Optional[str] = None
    approved: bool = Field(default=False)
    admin: bool = Field(default=False)
    encrypted_password: str

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_uuid: uuid.UUID = Field(default_factory=uuid.uuid4, index=True, unique=True) # Changed from uuid to user_uuid
    current_rating: Optional[float] = Field(default=1500.0)

    rankings: List["Ranking"] = Relationship(back_populates="user")
    # Use simple string name for link_model
    matches: List["Match"] = Relationship(back_populates="users", link_model="MatchUserLink")
    won_matches: List["Winner"] = Relationship(back_populates="user")

    @property
    def preferred_name(self) -> str:
        return self.nickname if self.nickname else self.name if self.name else "" # Added handling for name being None

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    user_uuid: uuid.UUID # Changed
    current_rating: Optional[float]
    num_matches: int = 0
    num_wins: int = 0
    num_losses: int = 0
    preferred_name: str = ""

class UserReadWithDetails(UserRead):
    rankings: List["RankingRead"] = []
    matches: List["MatchReadWithoutUsers"] = []

class UserUpdate(SQLModel):
    email: Optional[str] = None
    name: Optional[str] = None
    nickname: Optional[str] = None
    approved: Optional[bool] = None
    admin: Optional[bool] = None
    password: Optional[str] = None

class UserReadBasic(SQLModel):
    id: int
    user_uuid: uuid.UUID # Changed
    name: Optional[str]
    nickname: Optional[str]
    current_rating: Optional[float]

    @property
    def preferred_name(self) -> str:
        return self.nickname if self.nickname else self.name if self.name else ""
