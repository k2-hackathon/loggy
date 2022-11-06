from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from models.mixins import TimestampMixin
from database import base

class UserDetails(base, TimestampMixin):
    __tablename__ = "user_details"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=None, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=None)
    email = Column(String, nullable=None)
    
    users = relationship("User", back_populates="user_details")
