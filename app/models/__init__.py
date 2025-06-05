from .user import User, UserCreate, UserRead, UserReadWithDetails, UserUpdate, UserBase, UserReadBasic
from .match import Match, MatchCreate, MatchRead, MatchUpdate, MatchUserLink, MatchBase, MatchReadWithoutUsers
from .ranking import Ranking, RankingCreate, RankingRead, RankingBase
from .winner import Winner, WinnerCreate, WinnerRead, WinnerBase, WinnerReadBasic
from .test_model import TestTable # Added this line

print("Inside app/models/__init__.py: Importing models...")
