import sys 
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from src.drivers.interfaces.google_sheet_getter import GoogleSheetGetterInterface
from src.stages.contracts.extract_contract import ExtractContract
from datetime import date
from src.errors.extract_error import ExtractError


class ExtractScheduling:
    
    def __init__(self,google_sheet_getter:GoogleSheetGetterInterface ) ->None:    
        self.__google_sheet_getter = google_sheet_getter
        
    def extract(self) -> ExtractContract:
       #google_auth = self.__google_sheet_auth.get_service()
       try:
        scheduling_data = self.__google_sheet_getter.get_sheet()
        return ExtractContract(
            raw_information_content=scheduling_data,
            extraction_date=date.today()     
        )
       except Exception as exception:
           raise ExtractError(str(exception)) from exception