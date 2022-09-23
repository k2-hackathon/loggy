import datetime


class DynamodbRepository:
    """DynamoDBとのやりとりをここで行う
    - 軽度緯度情報を書き込む処理を行う
    - 緯度軽度情報を読み込む処理を行う
    """

    def create_geo_data(
        self,
        user_id: int,
        longitude: float,
        latitude: float,
        timestamp: datetime.datetime,
    ):
        # TODO: DynamoDBに位置情報を書き込む
        pass

    def get_geo_data(self, user_id: int):
        # TODO: DynamoDBから位置情報を取得する
        pass
