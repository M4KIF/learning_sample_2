from fastapi import FastAPI
import uvicorn

from feedback_platform.domains.inbox.adapters import InboxManagementAdapterFactory, TripcodeManagementAdapter
from feedback_platform.domains.inbox.app import InboxApplication
from feedback_platform.infrastructure.persistence.repositories import InboxRepository
from feedback_platform.infrastructure.persistence.connectors import sessionmanager

from typing import Annotated
from contextlib import asynccontextmanager

from feedback_platform.infrastructure.persistence.connectors import get_db_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

DBSessionDep = Annotated[AsyncSession, Depends(get_db_session)]

class App:
    def __init__(self):
        self.fastapi = FastAPI(lifespan=self.lifespan, title="feedback_platform", docs_url="/api/docs")
            # Inbox V1
        inbox_management_adapter = InboxManagementAdapterFactory(InboxRepository())
        tripcode_management_adapter = TripcodeManagementAdapter()
        inbox_app = InboxApplication(
            inbox_management=inbox_management_adapter,
            tripcode_management=tripcode_management_adapter)
        self.fastapi.include_router(inbox_app.get_rest_v1_router(), prefix="/api/v1", tags=["inbox"])

    
    @asynccontextmanager
    async def lifespan(self, app: FastAPI):
        """
        Function that handles startup and shutdown events.
        To understand more, read https://fastapi.tiangolo.com/advanced/events/
        """
        yield
        if sessionmanager._engine is not None:
            # Close the DB connection
            await sessionmanager.close()

def main():
    app = App()

    uvicorn.run(app.fastapi, host="0.0.0.0", port=8081)

main()