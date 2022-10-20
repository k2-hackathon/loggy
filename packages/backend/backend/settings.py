from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from common.settings import PostgreSQL

# 接続先DBの設定
DATABASE = f"postgresql://{PostgreSQL.USER}:{PostgreSQL.PASSWORD}@{PostgreSQL.HOST}:{PostgreSQL.PORT}/{PostgreSQL.DB_NAME}"

# Engine の作成
Engine = create_engine(DATABASE, encoding="utf-8", echo=False)
Base = declarative_base()