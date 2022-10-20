from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models.common import TimestampMixin
from settings import Base


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True, nullable=None)
    name = Column(String, nullable=None)

    lodgings = relationship("Lodging", back_populates="users")
    stays = relationship("Stay", back_populates="users")

class Lodging(Base, TimestampMixin):
    __tablename__ = "lodgings"
    
    id = Column(UUID, primary_key=True, index=True, nullable=None)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=None)
    
    users = relationship("User", back_populates="lodgings")

class Stay(Base, TimestampMixin):
    __tablename__ = "stays"

    id = Column(UUID, primary_key=True, index=True, nullable=None)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=None)
    
    users = relationship("User", back_populates="stays")
