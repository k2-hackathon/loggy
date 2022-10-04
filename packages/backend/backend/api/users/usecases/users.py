from api.users.services.users import UserDataService
from api.users.models.users import GetUserRequestModel


def get_users(user_id: str) -> str:
    service = UserDataService()
    response = service.get_user_profile(GetUserRequestModel(user_id=user_id))
    return response


def create_users(user_id: str, username: str, mail: str) -> None:
    service = UserDataService()
    service.create_user(user_id=user_id, username=username, mail=mail)
