from clients.dynamodb import dynamodb

from ..schema.geography import GeographyModel


class GeographyService:
    def create_geography(self, request_data: GeographyModel):
        """DynamoDBに位置情報の生データを書き込む処理をここに書く"""
        item = {
            "user_id": request_data.user_id,
            "timestamp": request_data.timestamp,
            "data": {
                "longitude": request_data.longitude,
                "latitude": request_data.latitude,
            },
        }
        table = dynamodb.Table("Geography")
        table.put_item(Item=item)
        return None
