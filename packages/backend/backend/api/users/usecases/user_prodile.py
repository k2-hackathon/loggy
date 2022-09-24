from api.users.services.users import UserDataService

def get_users(user_id: int):
    service = UserDataService()
    response = service.get_user_profile(user_id)
    return response

def create_users(user_id: int, mail: str):
    service = UserDataService()
    response = service.create_user(user_id=user_id, mail=mail)
    return response