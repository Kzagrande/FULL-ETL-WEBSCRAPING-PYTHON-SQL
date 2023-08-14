from datetime import datetime
from typing import Dict
import pandas as pd
import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.drivers.interfaces.wms_report_upload import WmsReportUploadInterface


class WmsReportUpload(WmsReportUploadInterface):
        
    @classmethod    
    def upload_sheet(cls, filename:str):
        sheet_path = 'C:\\Users\\User\\Downloads\\' + filename
        
        sheet_data = pd.read_excel(sheet_path)
        return sheet_data
        
