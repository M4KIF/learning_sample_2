from .rest import InboxRestWebApiV1, InboxManagementAdapterFactory
from fastapi import APIRouter
from feedback_platform.domains.inbox.core.ports import TripcodeManagement

class InboxApplication():

    def __init__(self, inbox_management: InboxManagementAdapterFactory, tripcode_management: TripcodeManagement):
        self.api_rest_v1: InboxRestWebApiV1 = InboxRestWebApiV1(inbox_management_adapter_factory=inbox_management, 
            tripcode_management_adapter=tripcode_management)

    def get_rest_v1_router(self) -> APIRouter:
        return self.api_rest_v1.router