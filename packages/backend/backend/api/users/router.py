from fastapi import APIRouter

from api.users.usecases.users import get_user, create_user

router = APIRouter()

router.get("/users/{user_id}")(get_user)
router.post("/users/{user_id}")(create_user)
