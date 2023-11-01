import sys
project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
import pandas as pd
from src.stages.contracts.transform_contract import TransformContract
from typing import List
from datetime import datetime
from src.errors.error_log import ErrorLog
from src.drivers.time_interval import get_current_and_last_hour


class TransformPutaway:
    def transform(self, extract_putaway: ExtractContract) -> TransformContract:
        transformed_data = self.__filter_and_transform_data(extract_putaway)
        transformed_data_contract = TransformContract(load_content=transformed_data)
        print("transformed data -->>", transformed_data_contract)
        return transformed_data_contract

    def __filter_and_transform_data(self, extract_putaway: ExtractContract) -> List:
        try:
            data_content = extract_putaway.raw_information_content

            data_content.fillna('', inplace=True)
            data_content["Operation time"].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content["sector"] = "putaway"
            data_content["current_date_"] = datetime.now().strftime("%Y-%m-%d")
            hours = data_content['Operation time'][0]
            hours_date_type = datetime.strptime(hours, "%Y-%m-%d %H:%M:%S")
            print(type(hours_date_type))
            print(hours_date_type)
            hours_date_type = hours_date_type.replace(minute=0, second=0, microsecond=0).replace(minute=0, second=0, microsecond=0)
            data_content["extraction_hour"] = hours_date_type
            print(data_content)
            excel_file = "putaway.xlsx"
            data_content.to_excel(excel_file, index=False)
            data_content_list = data_content.values.tolist()
            return data_content_list

        except Exception as exception:
            raise ErrorLog(
                str(exception), func=" __filter_and_transform_data - Putaway",error_code=17
            ) from exception
