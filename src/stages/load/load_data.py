from src.infra.interface.database_repository import DatabaseRepositoryInterface
from src.stages.contracts.transform_contract import TransformContract
from typing import Dict


class LoadData:
    def __init__(self, repository: DatabaseRepositoryInterface) -> None:
        self.__repository = repository

    def load(self, transformed_data_contract: TransformContract) -> None:
        load_content = transformed_data_contract.load_content
        print(type(load_content))
        self.__repository.insert_data(load_content)

    def truncate(self) -> None:
        self.__repository.truncate_tables()

    def procedure(self) -> None:
        self.__repository.run_procedure()
        
    def table_control(self,sector_infos:Dict) -> None:
        self.__repository.insert_in_table_control(sector_infos)
