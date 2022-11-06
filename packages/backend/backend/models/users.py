from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from models.mixins import TimestampMixin
from database import base


class User(base, TimestampMixin):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=None)
    name = Column(String, nullable=None)

    user_details = relationship("UserDetails", back_populates="users")
    lodgings = relationship("Lodging", back_populates="users")
    stays = relationship("Stay", back_populates="users")
