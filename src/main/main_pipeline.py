import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from src.stages.extract.extract import Extract
from src.stages.extract.extract import ExtractHc
from src.stages.transform.transform_rc_managment import TransformRcManagement
from src.stages.transform.transform_sorting_in import TransformSorting
from src.stages.transform.transform_putaway import TransformPutaway
from src.stages.transform.transform_consolidation import TransformConsolidation
from src.stages.transform.transform_picking import TransformPicking
from src.stages.transform.transform_sorting_out import TransformSortingOut
from src.stages.transform.transform_packing import TransformPacking
from src.stages.transform.transform_hc import TransformHc
from src.stages.load.load_data import LoadData
from src.drivers.rc_management import RcManagement
from src.drivers.sorting_in import SortingIn
from src.drivers.putaway import Putaway
from src.drivers.consolidation import Consolidation
from src.drivers.picking import Picking
from src.drivers.sorting_out import SortingOut
from src.drivers.packing import Packing
from src.drivers.google_sheet_getter import GoogleSheetGetter
from src.drivers.wms_report_upload import WmsReportUpload
from src.infra.database_connector import DatabaseConnection
from src.infra.database_repository import DatabaseRepository
from src.queries.queries import INSERT_RC_MANAGEMENT as rc_management_query
from src.queries.queries import INSERT_SORTING_IN as sorting_in_query
from src.queries.queries import INSERT_PUTAWAY as putaway_query
from src.queries.queries import INSERT_CONSOLIDATION as consolidation_query
from src.queries.queries import INSERT_PICKING as picking_query
from src.queries.queries import INSERT_SORTING_OUT as sorting_out_query
from src.queries.queries import INSERT_PACKING as packing_query
from src.queries.queries import INSERT_HC as hc_query
from src.queries.queries import TRUNCATE_TABLE as truncate_query
from src.queries.queries import RUN_PROCEDURE as procedure_query
from src.errors.error_log import ErrorLog
from datetime import datetime
from src.drivers.time_interval import get_current_and_last_hour
from typing import List


class MainPipeline:
    def get_pending_automations(self):
        sectors = {
            "Rc_management": self.rc_management,
            "Sorting_in": self.sorting_in,
            "Putaway": self.putaway,
            # "Consolidation": self.consolidation,
            "Picking": self.picking,
            "Sorting_out": self.sorting_out,
            "Packing": self.packing,
        }

        DatabaseConnection.connect()
        cursor = DatabaseConnection.connection.cursor()
        current_time = datetime.now()
        query = "SELECT id,sector,extraction_hour,nave FROM ware_ods_shein.rpa_control_naves WHERE extraction_hour <= %s AND status = False"
        cursor.execute(query, (current_time,))
        pending_automations = cursor.fetchall()

        for id, sector_name, extaction_hour,nave in pending_automations:
            try:
                print(id)
                print(pending_automations)
                DatabaseConnection.connect()
                cursor = DatabaseConnection.connection.cursor()
                truncate_sectors = LoadData(DatabaseRepository(query=truncate_query))
                truncate_sectors.truncate()
                # print(id)
                # print(sector_name)
                # print(extaction_hour)
                sector = sectors[sector_name]
                sector(extaction_hour,nave)
                self.hc()
                self.procedures()
                update_query = f"UPDATE ware_ods_shein.rpa_control_naves SET status = True WHERE id = {id}"
                cursor.execute(update_query)
                DatabaseConnection.connection.commit()
                DatabaseConnection.connection.close()
                print(
                    f"A extração do {sector_name} referente ás {extaction_hour} foi executada com sucesso e id {id}"
                )

            except Exception as exception:
                print(exception.error_code)
                if exception.error_code == 1:
                    update_query = f"UPDATE ware_ods_shein.rpa_control_naves SET status = True WHERE id = {id}"
                    cursor.execute(update_query)
                    print(
                        f"A extração do {sector_name} referente ás {extaction_hour} foi executada com sucesso"
                    )
                    DatabaseConnection.connection.commit()
                else:
                    ErrorLog(
                        message="Erro no pipeline",
                        func=f"get_pending_automations ERROR",
                        error_code=exception.error_code,
                    )


    def rc_management(self, pending=None,nave = None):
        try:
            print(nave)
            print(pending)
            extract_rc_contract = Extract(RcManagement(pending,nave), WmsReportUpload())
            transform_rc = TransformRcManagement()
            load_sorting = LoadData(DatabaseRepository(query=rc_management_query))
            extract_rc_contract = extract_rc_contract.extract()
            transform_rc_in_contract = transform_rc.transform(
                extract_rc_contract
            )
            load_sorting.load(transform_rc_in_contract)
        except Exception as exception:
            raise ErrorLog(
                str(exception),
                func="Pipeline - Rc_management",
                error_code=exception.error_code,
            )


    def sorting_in(self, pending=None,nave = None):
        try:
            print(nave)
            print(pending)
            extract_sorting = Extract(SortingIn(pending,nave), WmsReportUpload())
            transform_sorting = TransformSorting()
            load_sorting = LoadData(DatabaseRepository(query=sorting_in_query))
            extract_sorting_in_contract = extract_sorting.extract()
            transform_sorting_in_contract = transform_sorting.transform(
                extract_sorting_in_contract
            )
            load_sorting.load(transform_sorting_in_contract)
        except Exception as exception:
            raise ErrorLog(
                str(exception),
                func="Pipeline - Sorting_in",
                error_code=exception.error_code,
            )

    def putaway(self, pending=None,nave = None):
        try:
            print(pending)
            extract_putaway = Extract(Putaway(pending,nave), WmsReportUpload())
            transform_putaway = TransformPutaway()
            load_putaway = LoadData(DatabaseRepository(query=putaway_query))
            extract_putaway_in_contract = extract_putaway.extract()
            transform_putaway_in_contract = transform_putaway.transform(
                extract_putaway_in_contract
            )
            load_putaway.load(transform_putaway_in_contract)
        except Exception as exception:
            raise ErrorLog(
                str(exception),
                func="Pipeline - Putaway",
                error_code=exception.error_code,
            )
            
            
    # def consolidation(self, pending=None,nave = None):
    #     try:
    #         print(pending)
    #         extract_consolidation = Extract(Consolidation(pending,nave), WmsReportUpload())
    #         transform_consolidation = TransformConsolidation()
    #         load_putaway = LoadData(DatabaseRepository(query=consolidation_query))
    #         extract_consolidation_in_contract = extract_consolidation.extract()
    #         transform_consolidation_in_contract = transform_consolidation.transform(
    #             extract_consolidation_in_contract
    #         )
    #         load_putaway.load(transform_consolidation_in_contract)
    #     except Exception as exception:
    #         raise ErrorLog(
    #             str(exception),
    #             func="Pipeline - Consolidation",
    #             error_code=exception.error_code,
    #         )

    def picking(self, pending=None,nave = None):
        try:
            print(pending)
            extract_picking = Extract(Picking(pending,nave), WmsReportUpload())
            transform_picking = TransformPicking()
            load_picking = LoadData(DatabaseRepository(query=picking_query))
            extract_picking_in_contract = extract_picking.extract()
            transform_picking_in_contract = transform_picking.transform(
                extract_picking_in_contract
            )
            load_picking.load(transform_picking_in_contract)
        except Exception as exception:
            raise ErrorLog(
                str(exception),
                func="Pipeline - Picking",
                error_code=exception.error_code,
            )

    def sorting_out(self, pending=None,nave = None):
        try:
            extract_sorting_out = Extract(SortingOut(pending,nave), WmsReportUpload())
            transform_sorting_out = TransformSortingOut()
            load_sorting_out = LoadData(DatabaseRepository(query=sorting_out_query))
            extract_sorting_out_in_contract = extract_sorting_out.extract()
            transform_sorting_out_in_contract = transform_sorting_out.transform(
                extract_sorting_out_in_contract
            )
            load_sorting_out.load(transform_sorting_out_in_contract)
        except Exception as exception:
            raise ErrorLog(
                str(exception),
                func="Pipeline - Sorting_out",
                error_code=exception.error_code,
            )

    def packing(self, pending=None,nave = None):
        try:
            extract_paking = Extract(Packing(pending,nave), WmsReportUpload())
            transform_packing = TransformPacking()
            load_packing = LoadData(DatabaseRepository(query=packing_query))
            extract_paking_in_contract = extract_paking.extract()
            transform_packing_in_contract = transform_packing.transform(
                extract_paking_in_contract
            )
            load_packing.load(transform_packing_in_contract)
        except Exception as exception:
            raise ErrorLog(
                str(exception),
                func="Pipeline - Packing",
                error_code=exception.error_code,
            )

    # def backlog(self, pending=None):
    #     try:
    #         extract_backlog = ExtractBacklog(WmsBacklog())
    #         transform_backlog = TransformBacklog()
    #         load_backlog = LoadData(DatabaseRepository(query=backlog_query))
    #         extract_backlog_in_contract = extract_backlog.extract()
    #         transform_backlog_in_contract = transform_backlog.transform(
    #             extract_backlog_in_contract
    #         )
    #         load_backlog.load(transform_backlog_in_contract)
    #     except Exception as exception:
    #         raise ErrorLog(
    #             str(exception),
    #             func="Pipeline - Backlog",
    #             error_code=exception.error_code,
    #         )

    def hc(self):
        try:
            extract_hc = ExtractHc(GoogleSheetGetter(), WmsReportUpload())
            transform_hc = TransformHc()
            load_hc = LoadData(DatabaseRepository(query=hc_query))
            extract_hc_in_contract = extract_hc.extract()
            transform_hc_in_contract = transform_hc.transform(extract_hc_in_contract)
            load_hc.load(transform_hc_in_contract)
        except Exception as exception:
            raise ErrorLog(
                str(exception),
                func="Pipeline - Hc",
                error_code=exception.error_code,
            )

    def procedures(self):
        try:
            run_procedures = LoadData(DatabaseRepository(query=procedure_query))
            run_procedures.procedure()
        except Exception as exception:
            ErrorLog(str(exception), func="Pipeline - Procedures")

    def run_pipeline(self) -> None:
        self.get_pending_automations()
