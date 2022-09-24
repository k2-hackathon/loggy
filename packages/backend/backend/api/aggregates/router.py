from fastapi import APIRouter

from api.aggregates.usecases.lodgings import get_lodgings
from api.aggregates.usecases.stays import get_stays

router = APIRouter()

router.get("/aggregates/lodgings/{user_id}")(get_lodgings)
router.get("/aggregates/stays/{user_id}")(get_stays)