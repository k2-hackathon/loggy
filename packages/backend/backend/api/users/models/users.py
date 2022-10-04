from pydantic import BaseModel


class GetUserRequestModel(BaseModel):
    user_id: str


class GetUserResponseModel(BaseModel):
    user_id: str
    name: str


class CreateUserRequestModel(BaseModel):
    user_id: str
    username: str
    mail: str
