from feedback_platform.domains.inbox.core.ports import InboxManagement
from sqlalchemy.ext.asyncio import AsyncSession
from abc import ABC, abstractmethod
from uuid import UUID

# Utilizing duck typing to create a dependency injection point that requires
# as little maintanance as possible
class InboxRepository(ABC):

    @abstractmethod
    async def create(self, session:  AsyncSession, data: dict()) -> UUID:
        pass

    @abstractmethod
    async def update(self, session:  AsyncSession, data: dict()) -> dict():
        pass


class InboxManagementAdapterFactory:

    # Private port implementation class
    class _InboxManagementAdapter(InboxManagement):
    
        def __init__(self, repository: InboxRepository):
            self.repository = repository

        async def create_new_inbox(self, data: dict(), session: AsyncSession)  -> UUID:
            return await self.repository.create(session, data)

        async def update_inbox(self, data: dict()):
            return "altered"

        async def list_inboxes(self, data: dict()):
            return "listed"

    def __init__(self, repository: InboxRepository):
        self.repository = repository

    def new(self):
        return self._InboxManagementAdapter(repository=self.repository)