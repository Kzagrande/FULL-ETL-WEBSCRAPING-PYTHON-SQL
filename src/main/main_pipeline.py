import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)

from src.stages.extract.extract import Extract
from src.stages.transform.transform_sorting_in import TransformSorting
from src.stages.transform.transform_putaway import TransformPutaway
from src.stages.transform.transform_picking import TransformPicking
from src.stages.transform.transform_sorting_out import TransformSortingOut
from src.stages.load.load_data import LoadData
from src.drivers.sorting_in import SortingIn
from src.drivers.putaway import Putaway
from src.drivers.picking import Picking
from src.drivers.sorting_out import SortingOut
from src.drivers.wms_report_upload import WmsReportUpload
from src.infra.database_connector import DatabaseConnection
from src.infra.database_repository import DatabaseRepository
from src.queries.queries import INSERT_SORTING_IN as sorting_in_query
from src.queries.queries import INSERT_PUTAWAY as putaway_query
from src.queries.queries import INSERT_PICKING as picking_query
from src.queries.queries import INSERT_SORTING_OUT as sorting_out_query

class MainPipeline:
             
    def run_pipeline(self) -> None:
        DatabaseConnection.connect()
        
        extract_sorting = Extract(SortingIn(), WmsReportUpload())
        # transform_sorting = TransformSorting()
        # load_sorting = LoadData(DatabaseRepository(query=sorting_in_query))
        # extract_sorting_in_contract = extract_sorting.extract()
        # transform_sorting_in_contract = transform_sorting.transform(extract_sorting_in_contract)
        # load_sorting.load(transform_sorting_in_contract)
        
        
        # extract_putaway = Extract(Putaway(), WmsReportUpload())
        # transform_putaway = TransformPutaway()
        # load_putaway = LoadData(DatabaseRepository(query=putaway_query))
        # extract_putaway_in_contract = extract_putaway.extract()
        # transform_putaway_in_contract = transform_putaway.transform(extract_putaway_in_contract)
        # load_putaway.load(transform_putaway_in_contract)
        
        # extract_picking = Extract(Picking(), WmsReportUpload())
        # transform_picking = TransformPicking()
        # load_picking = LoadData(DatabaseRepository(query=picking_query))
        # extract_picking_in_contract = extract_picking.extract()
        # transform_picking_in_contract = transform_picking.transform(extract_picking_in_contract)
        # load_picking.load(transform_picking_in_contract)
        
        extract_sorting_out = Extract(SortingOut(), WmsReportUpload())
        transform_sorting_out = TransformSortingOut()
        load_picking = LoadData(DatabaseRepository(query=sorting_out_query))
        extract_sorting_out_in_contract = extract_sorting_out.extract()
        transform_sorting_in_out_in_contract = transform_sorting_out.transform(extract_sorting_out_in_contract)
        load_picking.load(transform_sorting_in_out_in_contract)
        
        
        