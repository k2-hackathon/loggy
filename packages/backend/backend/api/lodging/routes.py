from fastapi import APIRouter

from .usecases import get_lodgings

router = APIRouter()

router.get("/lodgings/{user_id}")(get_lodgings)
router.post("/lodgings/{user_id}")(get_lodgings)
router.put("/lodgings/{user_id}")(get_lodgings)
router.delete("/aggregates/{user_id}")(get_lodgings)
