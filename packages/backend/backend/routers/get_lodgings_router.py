from fastapi import APIRouter

router = APIRouter()


@router.get("/get/lodgings/{user_id}")
def get_lodgings(user_id: int):
    return "get_lodgings endpoint"

