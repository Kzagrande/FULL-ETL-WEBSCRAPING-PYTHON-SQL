from abc import ABC, abstractmethod
from typing import List

class DatabaseRepositoryInterface(ABC):

    @abstractmethod
    def insert_sorting_in(self, data: List) -> None:
        pass
