from api.users.services.users import UserDataService
from api.users.models.users import GetUserRequestModel, CreateUserRequestModel


def get_user(user_id: str) -> str:
    service = UserDataService()
    response = service.get_user_profile(GetUserRequestModel(user_id=user_id))
    return response


def create_user(user_id: str, name: str, mail: str) -> None:
    service = UserDataService()
    service.create_user(CreateUserRequestModel(user_id=user_id, name=name, mail=mail))
