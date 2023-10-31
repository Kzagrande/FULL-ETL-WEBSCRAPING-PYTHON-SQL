import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
import pandas as pd
from src.stages.contracts.transform_contract import TransformContract
from typing import List
from datetime import datetime
from src.errors.error_log import ErrorLog


class TransformPacking:
    def transform(self, extract_packing: ExtractContract) -> TransformContract:
        transformed_data = self.__filter_and_transform_data(extract_packing)
        transformed_data_contract = TransformContract(load_content=transformed_data)
        print("transformed data -->>", transformed_data_contract)
        return transformed_data_contract

    def __filter_and_transform_data(self, extract_packing: ExtractContract) -> List:
        try:
            data_content = extract_packing.raw_information_content
            columns_to_fill = [
                "Consolidational Order Recommendation Number",
                "Consolidational Package No.",
                "Sub-Package Number",
                "lack parcels during packing",
                "Workstation",
                "Operator",
            ]
            data_content.fillna('', inplace=True)
            data_content["Operation time"].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content["sector"] = "packing_"

            data_content["current_date_"] = datetime.now().strftime("%Y-%m-%d")
            
            hours = data_content.iloc[0,6] #operation time
            hours_date_type = datetime.strptime(hours, "%Y-%m-%d %H:%M:%S")
            print(type(hours_date_type))
            print(hours_date_type)
            hours_date_type = hours_date_type.replace(minute=0, second=0, microsecond=0).replace(minute=0, second=0, microsecond=0)
            data_content["extraction_hour"] = hours_date_type

            transformed_values = []
            for warehouse in data_content["Operator"]:
                if warehouse.startswith("SPglp2WH"):
                    transformed_value = "BR_GRU_SW 2"
                else:
                    transformed_value = "Sao Paulo GLP Transit Warehouse"
                transformed_values.append(transformed_value)

            # Adicionar a lista de valores transformados de volta ao DataFrame, se necessário
            data_content["Warehouse"] = transformed_values

            excel_file = "output.xlsx"
            data_content.to_excel(excel_file, index=False)
            data_content_list = data_content.values.tolist()
            return data_content_list

        except Exception as exception:
            raise ErrorLog(
                str(exception), func=" __filter_and_transform_data - Packing",error_code=15
            ) from exception
