
from feedback_platform.domains.inbox.core.ports import TripcodeManagement

class TripcodeManagementAdapter(TripcodeManagement):

    def __init__(self):
        pass

    @staticmethod
    def create_tripcode(username:str, password:str) -> str:
        return ""