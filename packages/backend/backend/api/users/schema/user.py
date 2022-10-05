from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    email: str


class GetResponseBody(BaseModel):
    users: List[User]


class PostRequestBody(BaseModel):
    name: str
    email: str


class PostResponseBody(BaseModel):
    user: User
