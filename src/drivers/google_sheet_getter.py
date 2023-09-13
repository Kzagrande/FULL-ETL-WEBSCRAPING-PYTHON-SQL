import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
import os
from src.drivers.google_sheet_auth import GoogleSheetAuth
from typing import List
import pandas as pd
from src.drivers.interfaces.google_sheet_getter import GoogleSheetGetterInterface
from src.errors.error_log import ErrorLog


class GoogleSheetGetter(GoogleSheetGetterInterface):
    def __init__(
        self,
    ):
        self.spreadsheet_id = "1BPJqdN2d_wTtJBktzWEtir0L1HkxMpGjTHqnSox7-c0"

    def get_sheet(self) -> List:
        try:
            auth = GoogleSheetAuth()
            self.service = auth.get_service()

            sheet = self.service.spreadsheets()
            result = (
                sheet.values()
                .get(
                    spreadsheetId=self.spreadsheet_id,
                    range="ATIVOS!A:R",  # Modificado para pegar todas as colunas de A a R
                )
                .execute()
            )
            values = result.get("values", [])

            if values:
                filtered_values = [
                    row for row in values if len(row) >= 1
                ]  # Filtra apenas as linhas com pelo menos 18 colunas preenchidas (de A a R)
                df = pd.DataFrame(filtered_values[1:], columns=filtered_values[0])
                download_path = os.path.expanduser("~") + "\\Downloads\\"
                excel_file = os.path.join(download_path, "hc.xlsx")
                df.to_excel(excel_file, index=False)
                print(f"Arquivo 'hc.xlsx' salvo em {excel_file}")
            else:
                print("No data found.")
        except Exception as exception:
            raise ErrorLog(str(exception), func="get_sheet()",error_code=7) from exception

        finally:
            return excel_file


# if __name__ == "__main__":

#     getter = GoogleSheetGetter()
#     getter.get_sheet()
