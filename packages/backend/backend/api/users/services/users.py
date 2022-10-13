# import psycopg2
# import psycopg2.extras
from common.settings import PostgreSQL


class UserDataService:
    """
    ユーザーデータに関するを処理をここで行う
    - ユーザーデータの取得
    - ユーザーデータの登録
    """

    # def get_user_profile(self, req: GetUserRequestModel) -> GetUserResponseModel:
    #     # TODO: postgreql.pyからデータを取得する
    #     # with psycopg2.connect(
    #     #     dbname=PostgreSQL.DB_NAME,
    #     #     user=PostgreSQL.USER,
    #     #     password=PostgreSQL.PASSWORD,
    #     #     host=PostgreSQL.HOST,
    #     #     port=PostgreSQL.PORT,
    #     # ) as conn:
    #     #     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as curs:
    #     #         query = f"SELECT user_id, name FROM users WHERE users.user_id = '{req.user_id}';"
    #     #         curs.execute(query)
    #     #         row_data = curs.fetchall()
    #     #         result = dict(row_data[0])  # dictに変換
    #     # return GetUserResponseModel(user_id=result["user_id"], name=result["name"])
    #     return []

    # def create_user(self, req: CreateUserRequestModel) -> list:
    #     # TODO: postgreql.pyでデータを書き込む
    #     # with psycopg2.connect(
    #     #     dbname=PostgreSQL.DB_NAME,
    #     #     user=PostgreSQL.USER,
    #     #     password=PostgreSQL.PASSWORD,
    #     #     host=PostgreSQL.HOST,
    #     #     port=PostgreSQL.PORT,
    #     # ) as conn:
    #     #     with conn.cursor() as curs:
    #     #         query = f"INSERT INTO users(user_id, name, mail)values('{req.user_id}', '{req.name}', '{req.mail}')"
    #     #         curs.execute(query)
    #     #         conn.commit()
    #     return []
