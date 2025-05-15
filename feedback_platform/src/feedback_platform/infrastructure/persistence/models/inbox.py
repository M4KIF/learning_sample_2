from sqlalchemy import Integer, String, UniqueConstraint, DateTime, UUID, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime
from . import Base

import uuid


class Inbox(Base):
    __tablename__ = "inbox"
    __table_args = (UniqueConstraint("uuid"))

    #id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    uuid: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    topic: Mapped[str] = mapped_column(String(128), nullable=False)
    signature: Mapped[str] = mapped_column(String(128), nullable=False)
    expiration_date: Mapped[int] = mapped_column(Integer)
    allow_anonymous_submissions: Mapped[bool] = mapped_column(Boolean)
    message = relationship("Message", back_populates="inbox", cascade="all, delete-orphan")
