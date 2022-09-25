from ..services.geography import GeographyService
from datetime import datetime
import hashlib
from ..models.geography import GeographyModel


def create_geography(user_id: str, longitude: str, latitude: str, date: datetime):
    timestamp = date.timestamp()
    request_data = GeographyModel(
        user_id=hashlib.md5(user_id.encode()).hexdigest(),
        longitude=longitude,
        latitude=latitude,
        timestamp=timestamp,
    )
    service = GeographyService()
    response = service.create_geography(request_data)
    return response
