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
