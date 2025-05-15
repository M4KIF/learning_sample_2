from sqlalchemy.ext.asyncio import AsyncSession
from feedback_platform.infrastructure.persistence.models import Inbox
from uuid import UUID
from asyncio import TaskGroup, Task

class InboxRepository():

    def __init__(self):
        pass

    async def create(self, session: AsyncSession, data: dict()) -> UUID:
        model = Inbox(**data)
        print(model)
        try:
            session.add(model)
            await session.commit()
            await session.refresh(model)
        except Exception as e:
            print(e.args)
        else:
            return model.uuid


    async def update(self, session: AsyncSession, data: dict()) -> dict():
        pass