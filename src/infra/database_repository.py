from typing import List, Dict
from .database_connector import DatabaseConnection
from .interface.database_repository import DatabaseRepositoryInterface
from src.errors.error_log import ErrorLog


class DatabaseRepository(DatabaseRepositoryInterface):
    def __init__(self, query: str) -> None:
        self.query = query

    def insert_data(self, data: List) -> None:
        try:
            print("DADO PARA ENTRAR NO DB -->>", data)
            print("DADO PARA ENTRAR NO DB -->>", type(data))
            cursor = DatabaseConnection.connection.cursor()
            cursor.executemany(self.query, list(data))
            DatabaseConnection.connection.commit()
        except Exception as exception:
            raise ErrorLog(str(exception), func="insert_data()",error_code=13) from exception

    def truncate_tables(self) -> None:
        try:
            __tables = [
                "rc_management",
                "sorting_in",
                "putaway",
                "consolidation",
                "picking",
                "sorting_out",
                "packing",
                "sectors_backlog",
                "hc",
            ]
            cursor = DatabaseConnection.connection.cursor()
            for table in __tables:
                self.query = f"TRUNCATE TABLE ware_ods_shein.{table}"
                print(self.query)
                cursor.execute(self.query)
                print(f"A tabela {table} foi truncada.")
            DatabaseConnection.connection.commit()
        except Exception as exception:
            raise ErrorLog(str(exception), func="truncate_tables()",error_code=10) from exception

    def run_procedure(self) -> None:
        try:
            cursor = DatabaseConnection.connection.cursor()
            cursor.execute(self.query)
            DatabaseConnection.connection.commit()
        except Exception as exception:
            raise ErrorLog(str(exception), func="run_procedure",error_code=11) from exception

    def insert_in_table_control(self, sector_infos: Dict) -> None:
        try:
            cursor = DatabaseConnection.connection.cursor()
            cursor.execute(self.query, sector_infos)
            DatabaseConnection.connection.commit()
        except Exception as exception:
            print(exception)
            raise ErrorLog(
                str(exception), func="insert_in_table_control",error_code=12
            ) from exception
