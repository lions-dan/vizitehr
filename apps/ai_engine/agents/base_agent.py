from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, user, clinic=None):
        self.user = user
        self.clinic = clinic

    @abstractmethod
    def handle_command(self, command: str) -> str:
        pass

