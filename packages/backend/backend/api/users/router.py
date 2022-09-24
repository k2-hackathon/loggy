from fastapi import APIRouter

from api.users.usecases.user_prodile import get_users, create_users

router = APIRouter()

router.get("/users/{user_id}")(get_users)
router.post("/users/{user_id}")(create_users)
