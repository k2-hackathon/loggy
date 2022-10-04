import psycopg2
from api.settings import PostgreSQL


class UserDataService:
    """
    ユーザーデータに関するを処理をここで行う
    - ユーザーデータの取得
    - ユーザーデータの登録
    """

    def get_user_profile(self, user_id: str):
        # TODO: postgreql.pyからデータを取得する
        with psycopg2.connect(
            dbname=PostgreSQL.DB_NAME,
            user=PostgreSQL.USER,
            password=PostgreSQL.PASSWORD,
            host=PostgreSQL.HOST,
            port=PostgreSQL.PORT,
        ) as conn:
            with conn.cursor() as curs:
                query = f"SELECT name FROM users WHERE users.user_id = '{user_id}';"
                curs.execute(query)
                data = curs.fetchall()
        return data

    def create_user(self, user_id: str, username: str, mail: str):
        # TODO: postgreql.pyでデータを書き込む
        with psycopg2.connect(
            dbname=PostgreSQL.DB_NAME,
            user=PostgreSQL.USER,
            password=PostgreSQL.PASSWORD,
            host=PostgreSQL.HOST,
            port=PostgreSQL.PORT,
        ) as conn:
            with conn.cursor() as curs:
                query = f"INSERT INTO users(user_id, name, mail)values('{user_id}', '{username}', '{mail}')"
                print(query)
                curs.execute(query)
                conn.commit()
