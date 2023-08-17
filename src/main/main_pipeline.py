import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)

from src.stages.extract.extract import Extract
from src.stages.transform.transform_sorting_in import TransformSorting
from src.stages.load.load_sorting_in import LoadData
from src.drivers.sorting_in import SortingIn
from src.drivers.wms_report_upload import WmsReportUpload
from src.infra.database_connector import DatabaseConnection
from src.infra.database_repository import DatabaseRepository
from src.queries.queries import INSERT_SORTING_IN as sorting_in_query

class MainPipeline:
    def __init__(self) -> None:
        self.__extract_sorting = Extract(SortingIn(), WmsReportUpload())
        self.__transform_sorting = TransformSorting()
        # query = '''
        #     INSERT INTO sorting_in
        #         (package_number, warehouse, order_number, shipping_mode, recomendation_zone, recomendation_lane, operated_by, operation_time, sector)
        #     VALUES
        #         (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        # '''
        self.__load_sorting = LoadData(DatabaseRepository(query=sorting_in_query))
        
    def run_pipeline(self) -> None:
        DatabaseConnection.connect()
        extract_sorting_in_contract = self.__extract_sorting.extract()
        transform_sorting_in_contract = self.__transform_sorting.transform(extract_sorting_in_contract)
        self.__load_sorting.load(transform_sorting_in_contract)