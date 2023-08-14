from abc import ABC, abstractmethod

class SortingInInterface(ABC):

    @abstractmethod
    def navigate_to_wms(self):
        pass

    @abstractmethod
    def sorting_in_workflow(self) -> None:
        pass