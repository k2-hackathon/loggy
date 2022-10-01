from pydantic import BaseModel


class GeographyModel(BaseModel):
    user_id: str
    longitude: str
    latitude: str
    timestamp: int
