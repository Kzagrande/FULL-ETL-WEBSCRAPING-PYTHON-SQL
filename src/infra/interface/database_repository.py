from abc import ABC, abstractmethod
from typing import List

class DatabaseRepositoryInterface(ABC):

    @abstractmethod
    def insert_data(self, data: List,query:str) -> None:
        pass
    
    def truncate_tables(self)-> None:
        pass
    
    def run_procedure(self)-> None:
        pass
