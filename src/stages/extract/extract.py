import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from datetime import date
from src.drivers.interfaces.web_driver_workflow import WebDriverWorkflowInterface
from src.drivers.interfaces.wms_report_upload import WmsReportUploadInterface
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError
from src.drivers.putaway import Putaway
from src.drivers.wms_report_upload import WmsReportUpload
from src.stages.transform.transform_sorting_in import TransformSorting
from src.stages.transform.transform_putaway import TransformPutaway

class Extract:

    def __init__(self, web_driver_workflow: WebDriverWorkflowInterface,wms_report_upload:WmsReportUploadInterface) -> None:
        self.__web_driver_workflow = web_driver_workflow
        self.__wms_report_upload = wms_report_upload
        
    def extract(self) -> ExtractContract:
        try:
            web_driver_workflow_information = self.__web_driver_workflow.web_drive_workflow()
            print(web_driver_workflow_information)
            essential_information = self.__wms_report_upload.upload_sclsheet(filename=web_driver_workflow_information)
            print(essential_information)
            return ExtractContract(
                raw_information_content=essential_information,
            )
        except Exception as exception:
            raise ExtractError(str(exception)) from exception


# if __name__ ==  "__main__":
#     test = Extract(Putaway(), WmsReportUpload())
#     extract_test = test.extract()
#     transform = TransformPutaway()
#     transformed_data = transform.transform(extract_test)
#     print(extract_test)