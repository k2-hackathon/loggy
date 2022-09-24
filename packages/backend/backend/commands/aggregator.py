from typing import List

class Aggregator:
    def __init__(self):
        # TODO: self.access_key = dynamoDB接続キー etc.
        # TODO: self.access_key = RDB接続キー etc.
        ...

    def get_geography(self):
        """DynamoDBからデータを取得する"""
        # data = sqlAlchemyなどのORMapperを使う
        ...

    def aggregate_lodgings(self, data: List):
        """lodgingsのデータを集計するメソッド"""
        ...

    def create_lodgings(self, agg_data: List):
        """集計されたlodgingsのデータをRDBに書き込むメソッド"""
        ...

    def aggregate_stays(self, data: List):
        """staysのデータを集計するメソッド"""
        ...

    def create_stays(self, agg_data: List):
        """集計されたのデータをRDBに書き込むメソッド"""
        ...

def aggregator():
    # agg = Aggregator()
    # data = agg.get_geography()

    # agg_lodge_data = agg.aggregate_lodgings(data)
    # agg.create_lodgings(agg_lodge_data)

    # agg_stays_data = agg.aggregate_stays(data)
    # agg.create_stays(agg_stays_data)
    print("command success")
