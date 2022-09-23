from fastapi import APIRouter


router = APIRouter()


@router.get("/auth/user/{user_id}")
def auth_user(user_id: int):
    return "auth_user endpoint"
