from fastapi import APIRouter

router = APIRouter()


@router.get("/get/user/{user_id}")
def get_users(user_id: int):
    return "get_users endpoint"
