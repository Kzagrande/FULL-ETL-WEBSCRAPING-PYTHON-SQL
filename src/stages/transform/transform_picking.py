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
            columns_to_fill = [
                "Transit warehouse",
                "Picking Group Number",
                "Picking Task No.",
                "Picking Methods",
                "Type",
                "Consolidational Order Recommendation Number",
                "Sub-Package Number",
                "Whether to short pick",
                "Picking Location",
                "Lane",
                "Picking area",
                "Picking Container",
                "Status",
                "Created by",
                "picker",
                "Picking Time",
                "Voided By",
                'Do you confirm to flag it as "cancel"?',
            ]
            data_content[columns_to_fill] = data_content[columns_to_fill].fillna("-")
            data_content["Task Creation Time"].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content["Task Pick-up Time"].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content["Voided Time"].fillna(
                datetime(1500, 1, 11, 11, 11, 11), inplace=True
            )
            data_content["sector"] = "picking"

            data_content["current_date_"] = datetime.now().strftime("%Y-%m-%d")
            hours = datetime.now()
            hours = hours.replace(minute=0, second=0, microsecond=0)

            data_content["extraction_hour"] = hours
            print(data_content)
            excel_file = "picking.xlsx"
            data_content.to_excel(excel_file, index=False)
            data_content_list = data_content.values.tolist()
            return data_content_list

        except Exception as exception:
            raise ErrorLog(
                str(exception), func=" __filter_and_transform_data - Picking"
            ) from exception
