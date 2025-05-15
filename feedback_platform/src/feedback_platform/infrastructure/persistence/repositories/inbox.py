from sqlalchemy.ext.asyncio import AsyncSession

class InboxRepository():

    def __init__(self):
        pass

    async def create(self, session: AsyncSession, data: dict()) -> str:
        pass

    async def update(self, session: AsyncSession, data: dict()) -> str:
        pass