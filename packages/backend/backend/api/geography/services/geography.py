from datetime import datetime
import boto3
import hashlib


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
        user_id: int,
        longitude: float,
        latitude: float,
        timestamp: datetime.timestamp,
    ):
        """DynamoDBに位置情報の生データを書き込む処理をここに書く"""
        # TODO: repository層のdynamodb.pyを呼び出して書き込みの処理をおく
        timestamp = timestamp.timestamp()
        geo_data = {
            "user_id": hashlib.md5(str(user_id).encode()).hexdigest(),
            "timestamp": int(timestamp),
            "data": {
                "longitude": str(longitude),
                "latitude": str(latitude),
            },
        }
        table = self.dynamodb.Table("Geography")
        table.put_item(Item=geo_data)
        return None
