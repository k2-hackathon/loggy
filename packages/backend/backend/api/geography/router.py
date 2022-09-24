from fastapi import APIRouter

from api.geography.usecases.geography import create_geography

router = APIRouter()

router.post("/geography/{user_id}")(create_geography)
