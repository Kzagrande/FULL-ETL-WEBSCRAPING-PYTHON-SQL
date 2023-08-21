import sys
project_root = 'C:\\Users\\User\\sites\\control-tower-D'
sys.path.insert(0, project_root)
from googleapiclient.errors import HttpError
from datetime import datetime
from src.drivers.google_sheet_auth import GoogleSheetAuth
from typing import List
import pandas as pd
from src.drivers.interfaces.google_sheet_getter import GoogleSheetGetterInterface
class GoogleSheetGetter(GoogleSheetGetterInterface):
    def __init__(self, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id

    def get_sheet_name(self):
        today = datetime.now()
        days_of_week = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
        day_name = days_of_week[today.isoweekday()]
        formatted_date =f"{day_name} {today.strftime('%m.%d')}"
        # print('formated date -->>>', formatted_date)
        return 'ATIVOS'

    
    def get_sheet(self) -> List:
        try:
            # Create an instance of GoogleSheetAuth to get the service
            auth = GoogleSheetAuth()
            self.service = auth.get_service()
            # print(self.service)

            # Call the Sheets API
            sheet = self.service.spreadsheets()
            result = sheet.values().get(
            spreadsheetId=spreadsheet_id,
            range='ATIVOS'
        ).execute()
            values = result.get('values', [])
            print('Values', values)
            excel_file = "test.xlsx"
            values.to_excel(excel_file, index=False)
        except HttpError as e:
            print('Error:', e)

# Exemplo de uso:
if __name__ == "__main__":
    spreadsheet_id = '1BPJqdN2d_wTtJBktzWEtir0L1HkxMpGjTHqnSox7-c0'
    updater = GoogleSheetGetter(spreadsheet_id)
    updater.get_sheet()
