import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from src.stages.extract.extract import Extract
from src.stages.extract.extract import ExtractHc
from src.stages.transform.transform_sorting_in import TransformSorting
from src.stages.transform.transform_putaway import TransformPutaway
from src.stages.transform.transform_picking import TransformPicking
from src.stages.transform.transform_sorting_out import TransformSortingOut
from src.stages.transform.transform_packing import TransformPacking
from src.stages.transform.transform_hc import TransformHc
from src.stages.load.load_data import LoadData
from src.drivers.sorting_in import SortingIn
from src.drivers.putaway import Putaway
from src.drivers.picking import Picking
from src.drivers.sorting_out import SortingOut
from src.drivers.packing import Packing
from src.drivers.google_sheet_getter import GoogleSheetGetter
from src.drivers.wms_report_upload import WmsReportUpload
from src.infra.database_connector import DatabaseConnection
from src.infra.database_repository import DatabaseRepository
from src.queries.queries import INSERT_SORTING_IN as sorting_in_query
from src.queries.queries import INSERT_PUTAWAY as putaway_query
from src.queries.queries import INSERT_PICKING as picking_query
from src.queries.queries import INSERT_SORTING_OUT as sorting_out_query
from src.queries.queries import INSERT_PACKING as packing_query
from src.queries.queries import INSERT_HC as hc_query
from src.queries.queries import TRUNCATE_TABLE as truncate_query
from src.queries.queries import RUN_PROCEDURE as procedure_query
from src.queries.queries import INSERT_INTO_TABLE_CONTROL as control_table_query
from src.errors.error_log import ErrorLog
from datetime import datetime



class MainPipeline:
    def automation_control(self, status: bool, sector: str) -> None:
        automation_control = LoadData(DatabaseRepository(query=control_table_query))
        sorting_in_infos = {
            "name": sector,
            "scheduled_time": {datetime.now()},
            "status": status,
        }
        sorting_values = (
            sorting_in_infos["name"],
            sorting_in_infos["scheduled_time"],
            sorting_in_infos["status"],
        )
        automation_control.table_control(sorting_values)

    def sorting_in(self):
        try:
            extract_sorting = Extract(SortingIn(), WmsReportUpload())
            transform_sorting = TransformSorting()
            load_sorting = LoadData(DatabaseRepository(query=sorting_in_query))
            extract_sorting_in_contract = extract_sorting.extract()
            transform_sorting_in_contract = transform_sorting.transform(
                extract_sorting_in_contract
            )
            load_sorting.load(transform_sorting_in_contract)
            self.automation_control(status=True, sector="Sorting_in")
        except Exception as exception:
            self.automation_control(status=False, sector="Sorting_in")
            ErrorLog(str(exception), func="Pipeline - Sorting_in")

    def putaway(self):
        try:
            extract_putaway = Extract(Putaway(), WmsReportUpload())
            transform_putaway = TransformPutaway()
            load_putaway = LoadData(DatabaseRepository(query=putaway_query))
            extract_putaway_in_contract = extract_putaway.extract()
            transform_putaway_in_contract = transform_putaway.transform(
                extract_putaway_in_contract
            )
            load_putaway.load(transform_putaway_in_contract)
            self.automation_control(status=True, sector="Putaway")
        except Exception as exception:
            self.automation_control(status=False, sector="Putaway")
            ErrorLog(str(exception), func="Pipeline - Putaway")

    def picking(self):
        try:
            extract_picking = Extract(Picking(), WmsReportUpload())
            transform_picking = TransformPicking()
            load_picking = LoadData(DatabaseRepository(query=picking_query))
            extract_picking_in_contract = extract_picking.extract()
            transform_picking_in_contract = transform_picking.transform(
                extract_picking_in_contract
            )
            load_picking.load(transform_picking_in_contract)
            self.automation_control(status=True, sector="Picking")
        except Exception as exception:
            self.automation_control(status=False, sector="Sorting_in")
            ErrorLog(str(exception), func="Pipeline - Picking")

    def sorting_out(self):
        try:
            extract_sorting_out = Extract(SortingOut(), WmsReportUpload())
            transform_sorting_out = TransformSortingOut()
            load_sorting_out = LoadData(DatabaseRepository(query=sorting_out_query))
            extract_sorting_out_in_contract = extract_sorting_out.extract()
            transform_sorting_out_in_contract = transform_sorting_out.transform(
                extract_sorting_out_in_contract
            )
            load_sorting_out.load(transform_sorting_out_in_contract)
            self.automation_control(status=True, sector="Sorting_out")
        except Exception as exception:
            self.automation_control(status=False, sector="Sorting_out")
            ErrorLog(str(exception), func="Pipeline - Sorting_out")

    def packing(self):
        try:
            extract_paking = Extract(Packing(), WmsReportUpload())
            transform_packing = TransformPacking()
            load_packing = LoadData(DatabaseRepository(query=packing_query))
            extract_paking_in_contract = extract_paking.extract()
            transform_packing_in_contract = transform_packing.transform(
                extract_paking_in_contract
            )
            load_packing.load(transform_packing_in_contract)
            self.automation_control(status=True, sector="Packing")
        except Exception as exception:
            self.automation_control(status=False, sector="Packing")
            ErrorLog(str(exception), func="Pipeline - Packing")

    def hc(self):
        try:
            extract_hc = ExtractHc(GoogleSheetGetter(), WmsReportUpload())
            transform_hc = TransformHc()
            load_hc = LoadData(DatabaseRepository(query=hc_query))
            extract_hc_in_contract = extract_hc.extract()
            transform_hc_in_contract = transform_hc.transform(extract_hc_in_contract)
            load_hc.load(transform_hc_in_contract)
        except Exception as exception:
            ErrorLog(str(exception), func="Pipeline - HC")

    def procedures(self):
        try:
            run_procedures = LoadData(DatabaseRepository(query=procedure_query))
            run_procedures.procedure()
        except Exception as exception:
            ErrorLog(str(exception), func="Pipeline - Procedures")


    def run_pipeline(self) -> None:
        DatabaseConnection.connect()
        truncate_sectors = LoadData(DatabaseRepository(query=truncate_query))
        truncate_sectors.truncate()
        self.sorting_in()
        self.putaway()
        self.picking()
        self.sorting_out()
        self.packing()
        self.hc()
        self.procedures()