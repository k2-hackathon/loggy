from fastapi import APIRouter
import datetime


router = APIRouter()


@router.post("/craete/lodgings/{user_id}")
def create_geo_data(
    user_id: int, longitude: float, latitude: float, timestamp: datetime.datetime
):
    return "create_geo_data endpoint"

