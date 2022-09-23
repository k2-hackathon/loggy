import datetime


class CreateGeoDataService:
    def create_geo_data(
        user_id: int, longitude: float, latitude: float, timestamp: datetime.datetime
    ):
        """DynamoDBに位置情報の生データを書き込む処理をここに書く"""
        # TODO: repository層のdynamodb.pyを呼び出して書き込みの処理をおく
        pass
