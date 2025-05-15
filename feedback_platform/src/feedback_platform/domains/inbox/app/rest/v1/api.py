from fastapi import APIRouter, Request, Response, Body
from feedback_platform.domains.inbox.core.use_cases import UsecaseFactory
from feedback_platform.domains.inbox.core.ports import InboxManagement, TripcodeManagement
from feedback_platform.domains.inbox.core.exceptions import FailedToStoreItem
from feedback_platform.infrastructure.persistence.dependencies import SqliteSessionDep
from sqlalchemy.ext.asyncio import AsyncSession
from abc import ABC, abstractmethod

from .dto import Creation, Modify

import pydantic

class InboxManagementAdapterFactory:
    @abstractmethod
    def new(self, session: AsyncSession) -> InboxManagement:
        pass

class InboxRestWebApiV1():

    # Orchestrate the dependencies and create router object
    def __init__(self, inbox_management_adapter_factory: InboxManagementAdapterFactory, tripcode_management_adapter: TripcodeManagement):
        self.router = APIRouter()
        self.inbox_management_adapter_factory = inbox_management_adapter_factory
        self.factory = UsecaseFactory(tripcode_management=tripcode_management_adapter)
        self.router.add_api_route("/inbox/", self.create_inbox, methods=["POST"])
        self.router.add_api_route("/inbox/", self.update_inbox, methods=["PUT"])
        self.router.add_api_route("/inbox/{userId}/list", self.retrieve_inbox_list, methods=["GET"])


    async def create_inbox(self, session: SqliteSessionDep, username: str, password: str, request: Request, response: Response, dto: pydantic.Json[Creation] = Body(...)):
        try:
            uuid = await self.factory.NewCreateInboxUseCase(
                self.inbox_management_adapter_factory.new()
                ).execute(dto.dict(), username, password, session)
        except FailedToStoreItem as e:
            response.status_code = 500
        else:
            response.status_code = 201
            response.body = str(uuid)
        return

    async def update_inbox(self, username: str, password: str, request: Request, response: Response, dto: pydantic.Json[Modify] = Body(...)):
        return {"reached": "yes"}

    async def retrieve_inbox_list(self):
        return {"reached": "yes"}