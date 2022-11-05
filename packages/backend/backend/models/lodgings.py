from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from models.mixins import TimestampMixin
from settings import Base

class Lodging(Base, TimestampMixin):
    __tablename__ = "lodgings"
    
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=None, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=None)
    
    users = relationship("User", back_populates="lodgings")
