from feedback_platform.domains.inbox.core.ports import InboxManagement
from sqlalchemy.ext.asyncio import AsyncSession
from abc import ABC, abstractmethod

# Utilizing duck typing to create a dependency injection point that requires
# as little maintanance as possible
class InboxRepository(ABC):

    @abstractmethod
    async def create(self, session:  AsyncSession, data: dict()) -> str:
        pass

    @abstractmethod
    async def update(self, session:  AsyncSession, data: dict()) -> str:
        pass


class InboxManagementAdapterFactory:

    # Private port implementation class
    class _InboxManagementAdapter(InboxManagement):
    
        def __init__(self, repository: InboxRepository, session:  AsyncSession):
            self.repository = repository
            self.session = session

        def create_new_inbox(self, data: dict()):
            return self.repository.create(self.session, data)

        def update_inbox(self, data: dict()):
            return "altered"

        def list_inboxes(self, data: dict()):
            return "listed"

    def __init__(self, repository: InboxRepository):
        self.repository = repository

    def new(self, session: AsyncSession):
        return self._InboxManagementAdapter(repository=self.repository, session=session)