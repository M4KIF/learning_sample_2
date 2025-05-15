from feedback_platform.domains.inbox.core.model import Inbox
from feedback_platform.domains.inbox.core.ports import InboxManagement, TripcodeManagement
from feedback_platform.domains.inbox.core.exceptions import FailedToStoreItem


class CreateInboxUseCase():
    
    def __init__(self, inbox_management: InboxManagement, tripcode_management: TripcodeManagement):
        self.inbox_management = inbox_management
        self.tripcode_management = tripcode_management

    async def execute(self, inbox_values: dict(), user: str, password: str) -> str:

        # Creating and populating the model
        print(inbox_values)
        inbox_values["signature"] = self.tripcode_management.create_tripcode(username=user, password=password)

        inbox = Inbox(**inbox_values)
        #inbox.signature = self.tripcode_management.create_tripcode(username=user, password=password)

        # Storing the created data
        try:
            await self.inbox_management.create_new_inbox(inbox.dict())
        except Exception as e:
            print("Failed to store an item :-> " + e.args())
            raise FailedToStoreItem()
        
        return str(inbox_values)