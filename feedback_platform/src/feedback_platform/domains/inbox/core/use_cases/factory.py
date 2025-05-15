from feedback_platform.domains.inbox.core.ports import InboxManagement, TripcodeManagement
from .create import CreateInboxUseCase

class UsecaseFactory():

    def __init__(self, tripcode_management: TripcodeManagement):
        self.tripcode_management = tripcode_management

    def NewCreateInboxUseCase(self, inbox_management: InboxManagement) -> CreateInboxUseCase:
        return CreateInboxUseCase(inbox_management, self.tripcode_management)