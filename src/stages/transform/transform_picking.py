import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
import pandas as pd
from src.stages.contracts.transform_contract import TransformContract
from typing import List
from datetime import datetime
from src.errors.error_log import ErrorLog


class TransformPicking:
    def transform(self, extract_picking: ExtractContract) -> TransformContract:
        transformed_data = self.__filter_and_transform_data(extract_picking)
        transformed_data_contract = TransformContract(load_content=transformed_data)
        print("transformed data -->>", transformed_data_contract)
        return transformed_data_contract

    def __filter_and_transform_data(self, extract_picking: ExtractContract) -> List:
        try:
            data_content = extract_picking.raw_information_content

            data_content.iloc[:,14].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content.iloc[:,15].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content.iloc[:,17].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content.iloc[:,19].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            
            data_content.iloc[:,4] = data_content.iloc[:,4].str.replace('.*多包.*', 'Multi-Order', regex=True)
            
            data_content["sector"] = "picking"
            data_content["current_date_"] = datetime.now().strftime("%Y-%m-%d")
            data_content.fillna('-', inplace=True)
            
            hours = data_content.iloc[0,17] #completion time
            hours_date_type = datetime.strptime(hours, "%Y-%m-%d %H:%M:%S")
            print(type(hours_date_type))
            print(hours_date_type)
            hours_date_type = hours_date_type.replace(minute=0, second=0, microsecond=0).replace(minute=0, second=0, microsecond=0)
            data_content["extraction_hour"] = hours_date_type
            print(data_content)
            excel_file = "picking.xlsx"
            data_content.to_excel(excel_file, index=False)
            data_content_list = data_content.values.tolist()
            return data_content_list

        except Exception as exception:
            raise ErrorLog(
                str(exception), func=" __filter_and_transform_data - Picking",error_code=16
            ) from exception
