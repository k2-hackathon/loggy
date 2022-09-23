class AuthUserService:
    def auth_user(self, user_id: int):
        """ここでユーザー認可の処理を行う.
        cognitoにアクセスして、user_tokenを取得する
        user_tokenをpostgreSQLのものと一致していることを確認する(?)
        一致していればOKである旨をレスポンスとして返す
        """
        pass
