from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from models.mixins import TimestampMixin
from database import base


class User(base, TimestampMixin):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=None)
    name = Column(String, nullable=None)

    lodgings = relationship("Lodging", back_populates="users")
    stays = relationship("Stay", back_populates="users")
