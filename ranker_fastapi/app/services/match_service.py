from typing import List, Optional, Tuple
from uuid import UUID
from sqlmodel import Session, select

from app.models.match import Match, MatchCreate, MatchRead, match_user_link_table
from app.models.user import User, UserReadBasic
from app.models.winner import Winner, WinnerCreate
from app.models.ranking import Ranking, RankingCreate # For updating rankings
from app.services.user_service import get_user # For user details. populate_user_read_details is not needed here.

# Placeholder for rating adjustment values
RATING_ADJUSTMENT_WINNER = 10
RATING_ADJUSTMENT_LOSER = -5

def create_match_service(db: Session, match_in: MatchCreate) -> Optional[Match]:
    if len(match_in.user_ids) != 2:
        return None

    user1 = get_user(db, match_in.user_ids[0])
    user2 = get_user(db, match_in.user_ids[1])
    winner_user: Optional[User] = None
    if hasattr(match_in, 'winner_id') and match_in.winner_id is not None:
        winner_user = get_user(db, match_in.winner_id)
    else:
        pass # Winner not provided at creation, match remains unconfirmed without winner.

    if not user1 or not user2:
        return None # One of the participating users not found

    if winner_user and winner_user.id not in match_in.user_ids:
        return None # Winner, if provided, must be one of the participants

    db_match = Match(confirmed=False) # Matches are unconfirmed initially
    db_match.users.append(user1)
    db_match.users.append(user2)

    db.add(db_match)
    db.commit()
    db.refresh(db_match)

    if winner_user: # If winner was provided and valid
        db_winner = Winner(user_id=winner_user.id, match_id=db_match.id)
        db.add(db_winner)
        db.commit()
        # db.refresh(db_winner) # Not strictly needed to refresh winner here

    return db_match

def get_match_service(db: Session, match_id: int) -> Optional[Match]:
    return db.get(Match, match_id)

def get_match_by_uuid_service(db: Session, match_uuid: UUID) -> Optional[Match]:
    statement = select(Match).where(Match.match_uuid == match_uuid)
    return db.exec(statement).first()

def get_matches_service(db: Session, skip: int = 0, limit: int = 100) -> List[Match]:
    statement = select(Match).offset(skip).limit(limit)
    matches = db.exec(statement).all()
    return list(matches)

def _update_ratings_and_create_rankings(db: Session, winner: User, loser: User):
    winner.current_rating = (winner.current_rating or 1500.0) + RATING_ADJUSTMENT_WINNER
    loser.current_rating = (loser.current_rating or 1500.0) + RATING_ADJUSTMENT_LOSER
    db.add(winner)
    db.add(loser)
    winner_ranking = Ranking(user_id=winner.id, rating=winner.current_rating)
    loser_ranking = Ranking(user_id=loser.id, rating=loser.current_rating)
    db.add(winner_ranking)
    db.add(loser_ranking)
    db.commit() # Commit rating and ranking changes
    db.refresh(winner)
    db.refresh(loser)

def approve_match_service(db: Session, match_uuid: UUID) -> Optional[Match]:
    db_match = get_match_by_uuid_service(db, match_uuid)
    if not db_match or db_match.confirmed:
        return None

    if not db_match.winner_record or not db_match.winner_record.user:
        return None # Match must have a winner to be approved

    winner_user = db_match.winner_record.user
    loser_user = None
    if len(db_match.users) == 2:
        if db_match.users[0].id == winner_user.id:
            loser_user = db_match.users[1]
        else:
            loser_user = db_match.users[0]

    if not loser_user:
        return None # Could not determine loser

    _update_ratings_and_create_rankings(db, winner_user, loser_user)

    db_match.confirmed = True
    db.add(db_match)
    db.commit() # Commit match confirmation
    db.refresh(db_match)
    return db_match

def populate_match_read_details(db: Session, db_match: Match) -> MatchRead:
    users_basic_info: List[UserReadBasic] = []
    for user_model in db_match.users:
        users_basic_info.append(
            UserReadBasic(
                id=user_model.id,
                user_uuid=user_model.user_uuid,
                name=user_model.name,
                nickname=user_model.nickname,
                current_rating=user_model.current_rating
            )
        )

    winner_basic_info: Optional[UserReadBasic] = None
    losing_user_basic_info: Optional[UserReadBasic] = None

    if db_match.winner_record and db_match.winner_record.user:
        winner_model = db_match.winner_record.user
        winner_basic_info = UserReadBasic(
            id=winner_model.id,
            user_uuid=winner_model.user_uuid,
            name=winner_model.name,
            nickname=winner_model.nickname,
            current_rating=winner_model.current_rating
        )
        for user_model in db_match.users:
            if user_model.id != winner_model.id:
                losing_user_basic_info = UserReadBasic(
                    id=user_model.id,
                    user_uuid=user_model.user_uuid,
                    name=user_model.name,
                    nickname=user_model.nickname,
                    current_rating=user_model.current_rating
                )
                break

    return MatchRead(
        id=db_match.id,
        match_uuid=db_match.match_uuid,
        confirmed=db_match.confirmed,
        users=users_basic_info,
        winner=winner_basic_info,
        losing_user=losing_user_basic_info
    )
print('[services/match_service.py] Created.')
