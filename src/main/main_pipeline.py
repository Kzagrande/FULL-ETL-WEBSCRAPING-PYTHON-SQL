import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)

from src.stages.extract.extract import Extract
from src.stages.transform.transform_sorting_in import TransformSorting
from src.stages.transform.transform_putaway import TransformPutaway
from src.stages.load.load_sorting_in import LoadData
from src.drivers.sorting_in import SortingIn
from src.drivers.putaway import Putaway
from src.drivers.wms_report_upload import WmsReportUpload
from src.infra.database_connector import DatabaseConnection
from src.infra.database_repository import DatabaseRepository
from src.queries.queries import INSERT_SORTING_IN as sorting_in_query
from src.queries.queries import INSERT_PUTAWAY as putaway_query

class MainPipeline:
             
    def run_pipeline(self) -> None:
        DatabaseConnection.connect()
        
        extract_sorting = Extract(SortingIn(), WmsReportUpload())
        transform_sorting = TransformSorting()
        load_sorting = LoadData(DatabaseRepository(query=sorting_in_query))
        extract_sorting_in_contract = extract_sorting.extract()
        transform_sorting_in_contract = transform_sorting.transform(extract_sorting_in_contract)
        load_sorting.load(transform_sorting_in_contract)
        
        
        extract_putaway = Extract(Putaway(), WmsReportUpload())
        transform_putaway = TransformPutaway()
        load_putaway = LoadData(DatabaseRepository(query=putaway_query))
        extract_putaway_in_contract = extract_putaway.extract()
        transform_putaway_in_contract = transform_putaway.transform(extract_putaway_in_contract)
        load_putaway.load(transform_putaway_in_contract)
        
        