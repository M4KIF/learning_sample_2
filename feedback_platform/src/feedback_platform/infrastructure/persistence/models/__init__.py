from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

from .inbox import Inbox
from .message import Message