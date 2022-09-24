from pydantic import BaseModel
from datetime import datetime


class GeographyModel(BaseModel):
    user_id: str
    longitude: str
    latitude: str
    timestamp: datetime.timestamp
