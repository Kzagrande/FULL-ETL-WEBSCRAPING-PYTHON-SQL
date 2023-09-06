from abc import ABC, abstractmethod

class WmsBacklogInterface(ABC):

    @abstractmethod
    def wait_for_element(self, by, value):
        pass

    @abstractmethod
    def extract_backlog(self) -> None:
        pass
    
    @abstractmethod
    def web_drive_workflow(self) -> None:
        pass
    
    