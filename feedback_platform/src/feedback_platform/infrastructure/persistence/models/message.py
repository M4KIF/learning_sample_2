from sqlalchemy import String, Integer, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base



class Message(Base):

    __tablename__ = "message"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(32), nullable=False)
    signature: Mapped[str] = mapped_column(String(128), nullable=False)
    inbox_uuid = Column(Integer, ForeignKey('inbox.uuid'))
    inbox = relationship("Inbox", back_populates="message")