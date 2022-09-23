from fastapi import APIRouter

router = APIRouter()


@router.get("/get/stays/{user_id}")
def get_stays(user_id: int):
    pass
