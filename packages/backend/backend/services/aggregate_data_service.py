class AggregateDataService:
    """集計データの取得に関する処理をここで行う
    - 滞在データの取得
    - 宿泊データの取得
    """

    def get_stays_data(self, user_id: int):
        # TODO: リポジトリ層のpostgresqlからstaysの集計データを取得する
        pass

    def get_lodgings_data(self, user_id: int):
        # TODO: リポジトリ層のpostgresqlからlodgingsの集計データを取得する
        pass
