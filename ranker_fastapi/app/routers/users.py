from typing import List, Optional, Union
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlmodel import Session
from app.db.database import get_db
from app.models.user import User, UserCreate, UserRead, UserUpdate
from app.services import user_service
router = APIRouter(prefix="/users", tags=["users"])
@router.post("/", response_model=UserRead)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_email(db, email=user.email)
    if db_user: raise HTTPException(status_code=400, detail="Email already registered")
    created_user = user_service.create_user(db=db, user_in=user)
    return user_service.populate_user_read_details(db=db, user=created_user)
@router.get("/", response_model=List[UserRead])
def read_users_list(approved: Optional[bool] = Query(None), skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_service.get_users(db, approved=approved, skip=skip, limit=limit)
    return [user_service.populate_user_read_details(db=db, user=u) for u in users]
@router.get("/{user_id_or_uuid}", response_model=UserRead)
def read_user_details(user_id_or_uuid: Union[UUID, int] = Path(...), db: Session = Depends(get_db)):
    db_user: Optional[User] = None
    if isinstance(user_id_or_uuid, UUID): db_user = user_service.get_user_by_uuid(db, user_uuid=user_id_or_uuid)
    else: db_user = user_service.get_user(db, user_id=user_id_or_uuid)
    if db_user is None: raise HTTPException(status_code=404, detail="User not found")
    return user_service.populate_user_read_details(db=db, user=db_user)
@router.put("/{user_id_or_uuid}", response_model=UserRead)
def update_existing_user(user_in: UserUpdate, user_id_or_uuid: Union[UUID, int] = Path(...), db: Session = Depends(get_db)):
    db_user: Optional[User] = None
    if isinstance(user_id_or_uuid, UUID): db_user = user_service.get_user_by_uuid(db, user_uuid=user_id_or_uuid)
    else: db_user = user_service.get_user(db, user_id=user_id_or_uuid)
    if not db_user: raise HTTPException(status_code=404, detail="User not found")
    updated_user = user_service.update_user(db=db, db_user=db_user, user_in=user_in)
    return user_service.populate_user_read_details(db=db, user=updated_user)
@router.get("/{user_uuid}/approve", response_model=UserRead)
def approve_user_route(user_uuid: UUID = Path(...), db: Session = Depends(get_db)):
    db_user = user_service.approve_user_service(db, user_uuid=user_uuid)
    if db_user is None: raise HTTPException(status_code=404, detail="User not found for approval")
    return user_service.populate_user_read_details(db=db, user=db_user)
print('[routers/users.py] Created.')
