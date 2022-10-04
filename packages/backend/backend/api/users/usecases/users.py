from api.users.services.users import UserDataService


def get_users(user_id: str):
    service = UserDataService()
    response = service.get_user_profile(user_id)
    return response


def create_users(user_id: str, username: str, mail: str):
    service = UserDataService()
    service.create_user(user_id=user_id, username=username, mail=mail)
