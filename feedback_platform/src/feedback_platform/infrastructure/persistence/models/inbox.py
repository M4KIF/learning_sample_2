from sqlalchemy import Integer, String, UniqueConstraint, DateTime, UUID
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime
from . import Base

import uuid


class Inbox(Base):
    __tablename__ = "inbox"
    __table_args = (UniqueConstraint("uuid"))

    #id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    uuid: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    signature: Mapped[str] = mapped_column(String(128), nullable=False)
    expiration_date: Mapped[datetime] = mapped_column(DateTime)
    messages = relationship("Messages", back_populates="inbox", cascade="all, delete-orphan")
