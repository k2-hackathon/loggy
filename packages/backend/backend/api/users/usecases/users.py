from typing import List
from uuid import UUID

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db

from ..schema.users import (User, UserCreateRequest, UserCreateResponse,
                            UserReadResponse)
from ..services.users import UserDataService

service = UserDataService()


def read_user(user_id: UUID, db: Session = Depends(get_db)) -> User:
    res = service.get_user_profile(db=db, user_id=user_id)
    return UserReadResponse(
        id=res.id, name=res.name, created_at=res.created_at, updated_at=res.updated_at
    )


def create_user(
    user_id: UUID, name: str, email: str, db: Session = Depends(get_db)
) -> UserCreateResponse:
    request = UserCreateRequest(id=user_id, name=name, email=email)
    db_user = service.get_user_profile(db=db, user_id=request.id)
    if db_user:
        raise HTTPException(status_code=400, detail="This user already registered.")
    res = service.create_user(db=db, request=request)
    return UserCreateResponse(
        id=res.id,
        name=res.name,
        created_at=res.created_at,
        updated_at=res.updated_at,
    )
