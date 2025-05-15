from abc import ABC, abstractstaticmethod

class InboxManagement(ABC):

    @abstractstaticmethod
    def create_new_inbox(self, data: dict()):
        pass

    @abstractstaticmethod
    def update_inbox(self, data: dict()):
        pass

    @abstractstaticmethod
    def list_inboxes(self, data: dict()):
        pass
