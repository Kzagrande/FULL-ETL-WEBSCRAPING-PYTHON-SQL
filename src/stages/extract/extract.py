import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from datetime import date
from src.drivers.interfaces.web_driver_workflow import WebDriverWorkflowInterface
from src.drivers.interfaces.wms_report_upload import WmsReportUploadInterface
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.error_log import ErrorLog
from src.drivers.interfaces.google_sheet_getter import GoogleSheetGetterInterface


class Extract:
    def __init__(
        self,
        web_driver_workflow: WebDriverWorkflowInterface,
        wms_report_upload: WmsReportUploadInterface,
    ) -> None:
        self.__web_driver_workflow = web_driver_workflow
        self.__wms_report_upload = wms_report_upload

    def extract(self) -> ExtractContract:
        try:
            web_driver_workflow_information = (
                self.__web_driver_workflow.web_drive_workflow()
            )
            print(web_driver_workflow_information)
            essential_information = self.__wms_report_upload.upload_sheet(
                filename=web_driver_workflow_information
            )
            print(essential_information)
            return ExtractContract(
                raw_information_content=essential_information,
            )
        except Exception as exception:
            raise ErrorLog(str(exception), func="Extract ERROR") from exception


class ExtractHc:
    def __init__(
        self,
        google_sheet_getter: GoogleSheetGetterInterface,
        wms_report_upload: WmsReportUploadInterface,
    ) -> None:
        self.__google_sheet_getter = google_sheet_getter
        self.__wms_report_upload = wms_report_upload

    def extract(self) -> ExtractContract:
        try:
            get_sheet_information = self.__google_sheet_getter.get_sheet()
            print(get_sheet_information)
            essential_information = self.__wms_report_upload.upload_sheet(
                filename="hc.xlsx"
            )
            return ExtractContract(
                raw_information_content=essential_information,
            )
        except Exception as exception:
            raise ErrorLog(str(exception), func="Extract HC ERROR") from exception


# if __name__ ==  "__main__":
#     test = Extract(Putaway(), WmsReportUpload())
#     extract_test = test.extract()
#     transform = TransformPutaway()
#     transformed_data = transform.transform(extract_test)
#     print(extract_test)
