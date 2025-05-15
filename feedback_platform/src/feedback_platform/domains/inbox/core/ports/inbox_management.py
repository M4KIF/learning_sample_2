from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import uuid4, UUID

class InboxManagement(ABC):

    @abstractmethod
    async def create_new_inbox(self, data: dict(), session: AsyncSession) -> UUID:
        pass

    @abstractmethod
    async def update_inbox(self, data: dict()):
        pass

    @abstractmethod
    async def list_inboxes(self, data: dict()):
        pass
