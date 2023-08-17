import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)

from src.stages.extract.extract import Extract
from src.stages.transform.transform_sorting_in import TransformSorting
from src.stages.load.load_sorting_in import LoadSorting_in
from src.drivers.sorting_in import SortingIn
from src.drivers.wms_report_upload import WmsReportUpload
from src.infra.database_connector import DatabaseConnection
from src.infra.database_repository import DatabaseRepository



class MainPipeline:
    def __init__(self) -> None:
        self.__extract_sorting = Extract(SortingIn(), WmsReportUpload())
        self.__transform_sorting = TransformSorting()
        self.__load_sorting = LoadSorting_in(DatabaseRepository())
        
    def run_pipeline(self) -> None:
        DatabaseConnection.connect()
        extract_sorting_in_contract = self.__extract_sorting.extract()
        transform_sorting_in_contract = self.__transform_sorting.transform(extract_sorting_in_contract)
        self.__load_sorting.load(transform_sorting_in_contract)