from sqlalchemy.orm import Session

from models import user_details, users

from ..schema.users import User, UserCreateRequest


class UserDataService:
    """
    ユーザーデータに関するを処理をここで行う
    - ユーザーデータの取得
    - ユーザーデータの登録
    """

    def get_user_profile(self, db: Session, user_id: str) -> dict:
        res = db.query(users.User).filter(users.User.id == user_id).first()
        if not res:
            return
        return res

    def create_user(self, db: Session, request: UserCreateRequest) -> None:
        user = users.User(id=request.id, name=request.name)
        user_details = user_details(id=request.id, email=request.email)
        try:
            db.add(user)
            db.add(user_details)
            db.commit()
            return
        except Exception as e:
            raise Exception(f"create user is failed. error message: {e}")
