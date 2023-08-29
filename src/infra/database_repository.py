from typing import List
from .database_connector import DatabaseConnection
from .interface.database_repository import DatabaseRepositoryInterface

class DatabaseRepository(DatabaseRepositoryInterface):

    def __init__(self,query:str) -> None:
        self.query = query 

    def insert_data(self, data: List) -> None:   
        
        print('DADO PARA ENTRAR NO DB -->>',data)
        cursor = DatabaseConnection.connection.cursor()
        for row in data:
            cursor.execute(self.query, list(row))

        DatabaseConnection.connection.commit()
        
                 
    def truncate_tables(self)  -> None:
         __tables = ['putaway', 'picking', 'sorting_out', 'packing', 'hc']
         cursor = DatabaseConnection.connection.cursor()
         for table in __tables:
            self.query = f"TRUNCATE TABLE ware_ods_shein.{table}" 
            print(self.query)
            cursor.execute(self.query)
            print(f"A tabela {table} foi truncada.")
         DatabaseConnection.connection.commit()
         
         
    def run_procedure(self) -> None:
        cursor  = DatabaseConnection.connection.cursor()
        cursor.execute(self.query)    
        DatabaseConnection.connection.commit() 