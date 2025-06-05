from typing import List, Optional
from uuid import UUID
from sqlmodel import Session, select, func, case
from passlib.context import CryptContext

from app.models.user import User, UserCreate, UserUpdate, UserRead
from app.models.ranking import Ranking, RankingCreate
from app.models.match import Match, match_user_link_table # Added match_user_link_table import
from app.models.winner import Winner # Needed for counts

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user_in: UserCreate) -> User:
    hashed_password = get_password_hash(user_in.password)
    user_data = user_in.model_dump(exclude={"password"})
    db_user = User(**user_data, encrypted_password=hashed_password, current_rating=1500.0)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    initial_ranking = Ranking(user_id=db_user.id, rating=db_user.current_rating)
    db.add(initial_ranking)
    db.commit()
    return db_user

def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.get(User, user_id)

def get_user_by_uuid(db: Session, user_uuid: UUID) -> Optional[User]:
    statement = select(User).where(User.user_uuid == user_uuid)
    return db.exec(statement).first()

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    statement = select(User).where(User.email == email)
    return db.exec(statement).first()

def get_users(db: Session, approved: Optional[bool] = None, skip: int = 0, limit: int = 100) -> List[User]:
    statement = select(User)
    if approved is not None:
        statement = statement.where(User.approved == approved)
    statement = statement.offset(skip).limit(limit)
    users = db.exec(statement).all()
    return list(users)

def update_user(db: Session, db_user: User, user_in: UserUpdate) -> User:
    user_data = user_in.model_dump(exclude_unset=True)
    if "password" in user_data and user_data["password"]:
        hashed_password = get_password_hash(user_data["password"])
        db_user.encrypted_password = hashed_password
        del user_data["password"]

    for key, value in user_data.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def approve_user_service(db: Session, user_uuid: UUID) -> Optional[User]:
    db_user = get_user_by_uuid(db, user_uuid)
    if db_user:
        db_user.approved = True
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    return db_user

def populate_user_read_details(db: Session, user: User) -> UserRead:
    num_matches_confirmed = db.exec(
        select(func.count(Match.id))
        .join(match_user_link_table, match_user_link_table.c.match_id == Match.id)
        .where(match_user_link_table.c.user_id == user.id)
        .where(Match.confirmed == True)
    ).one_or_none() or 0

    num_wins = db.exec(
        select(func.count(Winner.id))
        .where(Winner.user_id == user.id)
        .join(Match, Match.id == Winner.match_id)
        .where(Match.confirmed == True)
    ).one_or_none() or 0

    num_losses = num_matches_confirmed - num_wins

    return UserRead(
        id=user.id,
        user_uuid=user.user_uuid,
        email=user.email,
        name=user.name,
        nickname=user.nickname,
        approved=user.approved,
        admin=user.admin,
        encrypted_password=user.encrypted_password,
        current_rating=user.current_rating,
        num_matches=num_matches_confirmed,
        num_wins=num_wins,
        num_losses=num_losses,
        preferred_name=user.nickname if user.nickname else user.name if user.name else ""
    )
print('[services/user_service.py] Created.')
