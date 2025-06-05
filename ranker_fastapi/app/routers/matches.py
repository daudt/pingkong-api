from typing import List, Union, Optional # Added Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Path, Body
from sqlmodel import Session

from app.db.database import get_db
from app.models.match import Match, MatchCreate, MatchRead
from app.models.user import User # For current_user dependency later
from app.services import match_service

router = APIRouter(
    prefix="/matches",
    tags=["matches"],
)

@router.post("/", response_model=MatchRead)
def create_new_match(
    match_in: MatchCreate = Body(...),
    db: Session = Depends(get_db)
):
    if len(match_in.user_ids) != 2:
        raise HTTPException(status_code=400, detail="A match must have exactly two players.")
    if hasattr(match_in, 'winner_id') and match_in.winner_id and match_in.winner_id not in match_in.user_ids:
        raise HTTPException(status_code=400, detail="Winner must be one of the two players.")

    db_match = match_service.create_match_service(db=db, match_in=match_in)
    if not db_match:
        raise HTTPException(status_code=400, detail="Failed to create match. Invalid user IDs or winner ID.")
    return match_service.populate_match_read_details(db=db, db_match=db_match)

@router.get("/", response_model=List[MatchRead])
def read_matches_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    matches = match_service.get_matches_service(db, skip=skip, limit=limit)
    return [match_service.populate_match_read_details(db=db, db_match=m) for m in matches]

@router.get("/{match_id_or_uuid}", response_model=MatchRead)
def read_match_details(match_id_or_uuid: Union[UUID, int] = Path(...), db: Session = Depends(get_db)):
    db_match: Optional[Match] = None
    if isinstance(match_id_or_uuid, UUID):
        db_match = match_service.get_match_by_uuid_service(db, match_uuid=match_id_or_uuid)
    else:
        db_match = match_service.get_match_service(db, match_id=match_id_or_uuid)

    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return match_service.populate_match_read_details(db=db, db_match=db_match)

@router.get("/{match_uuid}/approve", response_model=MatchRead)
def approve_match_route(match_uuid: UUID = Path(...), db: Session = Depends(get_db)):
    approved_match = match_service.approve_match_service(db, match_uuid=match_uuid)
    if not approved_match:
        raise HTTPException(status_code=404, detail="Match not found or could not be approved.")
    return match_service.populate_match_read_details(db=db, db_match=approved_match)
print('[routers/matches.py] Created.')
