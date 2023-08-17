from abc import ABC, abstractmethod

class WebDriverWorkflowInterface(ABC):

    @abstractmethod
    def navigate_to_wms(self):
        pass

    @abstractmethod
    def web_drive_workflow(self) -> None:
        pass