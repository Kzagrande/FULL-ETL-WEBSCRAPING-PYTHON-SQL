import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from datetime import date
from src.drivers.interfaces.sorting_in import SortingInInterface
from src.drivers.interfaces.wms_report_upload import WmsReportUploadInterface
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError
from src.drivers.sorting_in import SortingIn
from src.drivers.wms_report_upload import WmsReportUpload
from src.stages.transform.transform_sorting_in import TransformSorting

class ExtractSortingIn:

    def __init__(self, sorting_in: SortingInInterface,wms_report_upload:WmsReportUploadInterface) -> None:
        self.__sorting_in = sorting_in
        self.__wms_report_upload = wms_report_upload
        
    def extract(self) -> ExtractContract:
        try:
            sorting_in_information = self.__sorting_in.sorting_in_workflow()
            print(sorting_in_information)
            essential_information = self.__wms_report_upload.upload_sheet(filename=sorting_in_information)
            return ExtractContract(
                raw_information_content=essential_information,
            )
        except Exception as exception:
            raise ExtractError(str(exception)) from exception



if __name__ ==  "__main__":
    test = ExtractSortingIn(SortingIn(), WmsReportUpload())
    extract_test = test.extract()
    transform = TransformSorting()
    transformed_data = transform.transform(extract_test)
    print(extract_test)
    