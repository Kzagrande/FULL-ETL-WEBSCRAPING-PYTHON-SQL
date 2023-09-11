import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
import pandas as pd
from src.stages.contracts.transform_contract import TransformContract
from typing import List
from datetime import datetime
from src.errors.error_log import ErrorLog


class TransformSortingOut:
    def transform(self, extract_sorting_out: ExtractContract) -> TransformContract:
        transformed_data = self.__filter_and_transform_data(extract_sorting_out)
        transformed_data_contract = TransformContract(load_content=transformed_data)
        print("transformed data -->>", transformed_data_contract)
        return transformed_data_contract

    def __filter_and_transform_data(self, extract_sorting_out: ExtractContract) -> List:
        try:
            data_content = extract_sorting_out.raw_information_content
            columns_to_fill = [
                "Warehouse",
                "task group number",
                "Picking Task No.",
                "Picking Container",
                "Package No.",
                "Sub-Package Number",
                "Basket number",
                "Whether to mark box empty names",
                "Sorted by",
            ]
            data_content[columns_to_fill] = data_content[columns_to_fill].fillna("-")
            data_content["Sorting Time"].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content["sector"] = "sorting_out"

            data_content["current_date_"] = datetime.now().strftime("%Y-%m-%d")
            hours = datetime.now()
            hours = hours.replace(minute=0, second=0, microsecond=0)
            data_content["extraction_hour"] = hours

            print(data_content)
            excel_file = "output.xlsx"
            data_content.to_excel(excel_file, index=False)
            data_content_list = data_content.values.tolist()
            return data_content_list

        except Exception as exception:
            raise ErrorLog(
                str(exception), func=" __filter_and_transform_data - Sorting_out"
            ) from exception
