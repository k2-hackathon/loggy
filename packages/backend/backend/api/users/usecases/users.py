from typing import List

from ..schema import GetResponseBody, PostRequestBody, PostResponseBody


def list_user(request) -> GetResponseBody:
    # service = UserDataService()
    # response = service.list_user_profile(GetUserRequestModel(user_id=user_id))
    response = GetResponseBody(users=[])
    return response


def create_user(request: PostRequestBody, *arg, **kwargs) -> PostResponseBody:
    data = PostRequestBody(*request)
    # service = UserDataService()
    # service.create_user(CreateUserRequestModel(user_id=user_id, name=name, mail=mail))
    response = PostResponseBody(
        user={"id": "12345667890", "name": data.name, "email": data.email}
    )
    return response
