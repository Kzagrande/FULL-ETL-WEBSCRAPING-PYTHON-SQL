from abc import ABC, abstractmethod
from typing import List,Dict

class DatabaseRepositoryInterface(ABC):

    @abstractmethod
    def insert_data(self, data: List,query:str) -> None:
        pass
    
    def truncate_tables(self)-> None:
        pass
    
    def run_procedure(self)-> None:
        pass
    
    def insert_in_table_control(self,sector_infos:Dict,query:str)->None:
        pass
