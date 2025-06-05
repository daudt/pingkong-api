from .user import User, UserCreate, UserRead, UserReadWithDetails, UserUpdate, UserBase, UserReadBasic
from .match import Match, MatchCreate, MatchRead, MatchUpdate, MatchBase, MatchReadWithoutUsers, match_user_link_table
from .ranking import Ranking, RankingCreate, RankingRead, RankingBase
from .winner import Winner, WinnerCreate, WinnerRead, WinnerBase, WinnerReadBasic
try:
    from .test_model import TestTable
except ImportError:
    pass # test_model.py might have been removed
print('[models/__init__.py] Recreated.')
