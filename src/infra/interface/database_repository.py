from abc import ABC, abstractmethod
from typing import List

class DatabaseRepositoryInterface(ABC):

    @abstractmethod
    def insert_data(self, data: List,query:str) -> None:
        pass
