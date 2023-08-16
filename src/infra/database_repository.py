from typing import List
from .database_connector import DatabaseConnection
from .interface.database_repository import DatabaseRepositoryInterface

class DatabaseRepository(DatabaseRepositoryInterface):

    @classmethod
    def insert_sorting_in(cls, data: List) -> None:   
        print(data)
        query = '''
            INSERT INTO sorting_in
                (package_number, warehouse, order_number, shipping_mode, recomendation_zone, recomendation_lane, operated_by, operation_time, sector)
            VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
        cursor = DatabaseConnection.connection.cursor()
        for row in data:
            cursor.execute(query, list(row))

        DatabaseConnection.connection.commit()
