import sys

project_root = "C:\\Users\\User\\sites\\control-tower-D"
sys.path.insert(0, project_root)
from src.stages.contracts.extract_contract import ExtractContract
from src.stages.contracts.transform_contract import TransformContract
from typing import List
from src.errors.error_log import ErrorLog


class TransformHc:
    def transform(self, extract_hc: ExtractContract) -> TransformContract:
        transformed_data = self.__filter_and_transform_data(extract_hc)
        transformed_data_contract = TransformContract(load_content=transformed_data)
        print("transformed data -->>", transformed_data_contract)
        return transformed_data_contract

    def __filter_and_transform_data(self, extract_hc: ExtractContract) -> List:
        try:
            data_content = extract_hc.raw_information_content
            columns_to_fill = [
                "NAME",
                "ID EMPLOYER",
                "ADMISSION DT",
                "COMPANY",
                "WH",
                "BZ",
                "COLLAR",
                "CATEGORY",
                "SECTOR",
                "ROLE",
                "SHIFT",
                "SCHEDULE",
                "MANAGER 1",
                "MANAGER 2",
                "MANAGER 3",
                "STATUS",
                "ROLE 2",
                "USER",
            ]
            data_content[columns_to_fill] = data_content[columns_to_fill].fillna("-")
            return data_content.values.tolist()
        except Exception as exception:
            raise ErrorLog(
                str(exception), func=" __filter_and_transform_data - HC",error_code=2
            ) from exception
