import boto3
import hashlib
from ..models.geography import GeographyModel

class GeographyService:
    def __init__(self):
        self.dynamodb = boto3.resource(
            service_name="dynamodb",
            endpoint_url="http://dynamodb:8000",
            aws_access_key_id="",
            aws_secret_access_key="",
            region_name="",
        )

    def create_geography(
        self,
        request_data: GeographyModel
    ):
        """DynamoDBに位置情報の生データを書き込む処理をここに書く"""
        item = {
            "user_id": request_data.user_id,
            "timestamp": request_data.timestamp,
            "data": {
                "longitude": request_data.longitude,
                "latitude": request_data.latitude,
            },
        }
        table = self.dynamodb.Table("Geography")
        table.put_item(Item=item)
        return None
