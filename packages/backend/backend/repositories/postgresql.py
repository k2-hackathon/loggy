class PostgresqlRepository:
    """PostgreSQLとのやりとりをここで行う
    - 滞在データの取得
    - 宿泊データの取得
    - ユーザーデータの取得
    - ユーザーデータの書き込み
    """

    def get_lodgings_data(self, user_id: int):
        # TODO: postgreSQLのlodgingsテーブルからユーザーIDに紐づくデータを取得して呼び出し元に返す
        pass

    def get_stays_data(self, user_id: int):
        # TODO: postgreSQLのstaysテーブルからユーザーIDに紐づくデータを取得して呼び出し元に返す
        pass

    def get_user_data(self, user_id: int):
        # TODO: postgreSQLのuserテーブルからユーザー名を取得して呼び出し元に返す
        pass

    def create_user_data(self, user_id: int, mail: str):
        # TODO: postgreSQLのuserテーブルに各種ユーザー情報を書き込む
        pass
