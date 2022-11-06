from datetime import datetime

from ..schema.geography import GeographyModel
from ..services.geography import GeographyService


def create_geography(user_id: str, longitude: str, latitude: str, date: datetime):
    timestamp = date.timestamp()
    request_data = GeographyModel(
        user_id=user_id,
        longitude=longitude,
        latitude=latitude,
        timestamp=timestamp,
    )
    service = GeographyService()
    response = service.create_geography(request_data)
    return response
