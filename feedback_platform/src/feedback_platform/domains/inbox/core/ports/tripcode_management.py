from abc import ABC, abstractmethod

class TripcodeManagement(ABC):

    @abstractmethod
    def create_tripcode(self, username:str, password:str) -> str:
        pass

