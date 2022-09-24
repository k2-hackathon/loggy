from ..services.geography import GeographyService
from datetime import datetime


def create_geography(
    user_id: int, longitude: float, latitude: float, timestamp: datetime
):
    service = GeographyService()
    response = service.create_geography(
        user_id, longitude=longitude, latitude=latitude, timestamp=timestamp
    )
    return response
