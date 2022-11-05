from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: UUID
    name: str
    email: str


class UserReadResponse(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime


class UserCreateRequest(BaseModel):
    id: UUID
    name: str
    email: str


class UserCreateResponse(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime
