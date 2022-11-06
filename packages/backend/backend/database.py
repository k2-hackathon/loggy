from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from common.settings import PostgreSQL

# 接続先DBの設定
DATABASE = f"postgresql://{PostgreSQL.USER}:{PostgreSQL.PASSWORD}@{PostgreSQL.HOST}:{PostgreSQL.PORT}/{PostgreSQL.DB_NAME}"

# engine の作成
engine = create_engine(DATABASE, encoding="utf-8", echo=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

base = declarative_base()

# Dependency Injection
def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()