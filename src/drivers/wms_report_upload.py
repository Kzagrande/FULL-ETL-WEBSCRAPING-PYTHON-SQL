import pandas as pd
import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.drivers.interfaces.wms_report_upload import WmsReportUploadInterface
from src.errors.error_log import ErrorLog


class WmsReportUpload(WmsReportUploadInterface):
        
    @classmethod    
    def upload_sheet(cls, filename:str):
        try:
            sheet_path = 'C:\\Users\\User\\Downloads\\' + filename   
            sheet_data = pd.read_excel(sheet_path)
        except Exception as exception:
            raise ErrorLog(
                str(exception), func="upload_sheet()",error_code=4
            ) from exception            
        return sheet_data
        
